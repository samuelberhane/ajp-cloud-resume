resource "google_project_service" "cloud_run_service" {
  project = var.project_id
  service = "run.googleapis.com"
}