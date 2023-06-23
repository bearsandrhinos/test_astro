FROM quay.io/astronomer/astro-runtime:8.4.0

ENV AIRFLOW__SECRETS__BACKEND="airflow.providers.google.cloud.secrets.secret_manager.CloudSecretManagerBackend"
ENV AIRFLOW__SECRETS__BACKEND_KWARGS='{"connections_prefix": "airflow-connections", "variables_prefix": "airflow-variables", "gcp_keyfile_dict": ${GCP_SECRET_MANAGER_SA_KEY}}'