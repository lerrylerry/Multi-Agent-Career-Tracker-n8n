import json
import os

# Define the exact data mapping matrix for find-and-replace cleanup
SENSITIVE_REPLACEMENTS = {
    # 1. Google Drive & Docs Asset IDs
    "1XQuRC3Ium3ldtPQNX0GGXpliVytMtFTQ6r4Q3IBqsEk": "YOUR_MASTER_KNOWLEDGE_BASE_DOC_ID",
    "1-4QpizEcc4MSuo7l-PDsSkIXqHHQBX5St6gdj2_8RaU": "YOUR_RESUME_MASTER_TEMPLATE_DOC_ID",
    "1GvcWKaqmhAprrkm37RL5Wd2DA-2k_y78": "YOUR_GOOGLE_DRIVE_TARGET_FOLDER_ID",

    # 2. Airtable Schema Structural Target IDs
    "appiMgjNKVK4zWAam": "YOUR_AIRTABLE_BASE_ID",
    "tblmpG78fjBjgpZ51": "YOUR_AIRTABLE_COMPANIES_TABLE_ID",
    "tblB6BqQAjwSpCEq4": "YOUR_AIRTABLE_JOBS_TABLE_ID",
    "tblPRZ9sRPQvQ1tmV": "YOUR_AIRTABLE_ANALYSIS_TABLE_ID",

    # 3. Private Telegram Operational Channel IDs
    "-1004329359747": "YOUR_TELEGRAM_LOW_MATCH_CHAT_ID",
    "-1004311183884": "YOUR_TELEGRAM_HIGH_MATCH_CHAT_ID",
    "-1003942376666": "YOUR_TELEGRAM_CRASH_REPORT_CHAT_ID"
}

def execute_pipeline_scrub(input_filename, output_filename):
    # Verify input file path exists before running string manipulations
    if not os.path.exists(input_filename):
        print(f"❌ Error: The source file '{input_filename}' was not found in this folder.")
        print("Please check the file name and run again.")
        return

    print(f"🔍 Initializing secure data scrub on: {input_filename}...")
    
    # Read the raw un-scrubbed JSON layout string
    with open(input_filename, 'r', encoding='utf-8') as file:
        raw_workflow_data = file.read()

    # Loop through the data matrix and execute deterministic replacements
    total_replacements_made = 0
    for target_secret, safe_placeholder in SENSITIVE_REPLACEMENTS.items():
        if target_secret in raw_workflow_data:
            occurrences = raw_workflow_data.count(target_secret)
            raw_workflow_data = raw_workflow_data.replace(target_secret, safe_placeholder)
            print(f"   ↳ Masked secret value spatial instances: [{safe_placeholder}] x{occurrences}")
            total_replacements_made += occurrences

    # Write out the clean sanitized blueprint document template
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(raw_workflow_data)

    print("\n" + "="*70)
    print(f"✅ Success! Purged {total_replacements_made} structural risk variables.")
    print(f"🔒 Sanitized JSON file is ready for GitHub distribution: '{output_filename}'")
    print("="*70)

if __name__ == "__main__":
    # CONFIGURATION: Change 'my_workflow.json' to match your actual downloaded n8n filename
    TARGET_INPUT_FILE = "my_workflow.json"
    SECURE_OUTPUT_FILE = "sanitized_career_tracker_workflow.json"
    
    execute_pipeline_scrub(TARGET_INPUT_FILE, SECURE_OUTPUT_FILE)
