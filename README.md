# KubeNSMigrator

KubeNSMigrator is a powerful tool designed for exporting and importing Kubernetes resources from specified namespaces. This tool helps you easily transfer resources between Kubernetes clusters, ensuring seamless migration and backup of your Kubernetes deployments.

## Features

- **Namespace-Specific Export**: Export resources from a specified namespace, excluding unnecessary ones.
- **ClusterIP Service Handling**: Automatically removes ClusterIP fields from exported Service resources to ensure compatibility during import.
- **Comprehensive Resource Support**: Supports a wide range of Kubernetes resources including deployments, services, secrets, persistentvolumeclaims, configmaps, statefulsets, daemonsets, ingresses, cronjobs, jobs, and persistentvolumes.
