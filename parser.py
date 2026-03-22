def normalize_config(config):
    normalized = {}
    for key, value in config.items():
        normalized[key.strip().lower()] = value
    return normalized

if __name__ == "__main__":
    print("Config parser running...")
