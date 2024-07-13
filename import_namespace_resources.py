import os
import subprocess
import sys
import datetime

# Check if target kubeconfig file and namespace are provided
if len(sys.argv) < 3:
    print("Usage: python3 import_namespace_resources.py <target-kubeconfig> <namespace>")
    sys.exit(1)

TARGET_KUBECONFIG = sys.argv[1]
NAMESPACE = sys.argv[2]

print(f"Using target kubeconfig file: {TARGET_KUBECONFIG}")
print(f"Importing resources to namespace: {NAMESPACE}")

# Directory containing exported YAMLs
EXPORT_DIR = f"exported_resources_{NAMESPACE}"
LOG_DIR = "import_logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Check if kubectl is installed
KUBECTL_PATH = subprocess.run(["which", "kubectl"], capture_output=True, text=True).stdout.strip()
if not os.path.isfile(KUBECTL_PATH) or not os.access(KUBECTL_PATH, os.X_OK):
    print("kubectl is not installed or not found in the PATH. Please install kubectl and try again.")
    sys.exit(1)

# Function to log import process
def log_import(file, content):
    with open(file, 'a') as log:
        log.write(content + "\n")

# Import resources for the specified namespace
log_file = os.path.join(LOG_DIR, f"import_log_{NAMESPACE}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log")

print(f"Importing resources to namespace {NAMESPACE}")
for filename in os.listdir(EXPORT_DIR):
    if filename.endswith(".yaml"):
        resource_file = os.path.join(EXPORT_DIR, filename)
        apply_cmd = [KUBECTL_PATH, "--kubeconfig", TARGET_KUBECONFIG, "apply", "-f", resource_file, "-n", NAMESPACE]
        result = subprocess.run(apply_cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Imported {filename} to namespace {NAMESPACE}")
            log_import(log_file, f"Imported {filename} to namespace {NAMESPACE}")
        else:
            print(f"Failed to import {filename}: {result.stderr}")
            log_import(log_file, f"Failed to import {filename}: {result.stderr}")

print("Import completed. Check logs for details.")
