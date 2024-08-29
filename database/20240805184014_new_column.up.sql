-- Add up migration script here
ALTER TABLE integrations
  ADD COLUMN access_token VARCHAR(255) NOT NULL;