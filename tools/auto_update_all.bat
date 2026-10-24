@echo off
echo ===================================================
echo     ECOS-SYNTHETICA MASTER ACADEMIC AUTO-UPDATER
echo ===================================================
echo.
echo [1/5] Initializing Syllabus Schema...
python tools\init_master_db.py

echo [2/5] Running Core Expansion Set 1...
python tools\expand_bank_volume.py

echo [3/5] Running Core Expansion Set 2...
python tools\expand_bank_volume_part2.py

echo [4/5] Running Algorithmic Matrix Generator...
python tools\auto_matrix_generator.py

@echo off
echo ===================================================
echo     ECOS-SYNTHETICA MASTER ACADEMIC AUTO-UPDATER
echo ===================================================
echo.
echo [1/6] Initializing Syllabus Schema...
python tools\init_master_db.py

echo [2/6] Running Core Expansion Set 1...
python tools\expand_bank_volume.py

echo [3/6] Running Core Expansion Set 2...
python tools\expand_bank_volume_part2.py

echo [4/6] Running Zoology & Human Physiology Batch 4...
python tools\ingest_batch4.py

echo [5/6] Running Algorithmic Matrix Generator...
python tools\auto_matrix_generator.py

echo [6/6] Exporting Chunks and Updating Game Manifest...
python tools\export_chunks.py

echo.
echo ===================================================
echo     SUMMARY OF ACTIVE CHAPTER VOLUMES
echo ===================================================
powershell -Command "(Get-Content data\manifest.json | ConvertFrom-Json) | Where-Object { $_.current_volume -gt 0 } | Format-Table -Property @{Label='Chapter Key'; Expression={$_.chapter_key}}, @{Label='Questions'; Expression={$_.current_volume}}, @{Label='Subject'; Expression={$_.subject}} -AutoSize"
pause
echo [5/5] Exporting Chunks and Updating Game Manifest...
python tools\export_chunks.py

echo.
echo ===================================================
echo     SUMMARY OF ACTIVE CHAPTER VOLUMES
echo ===================================================
powershell -Command "(Get-Content data\manifest.json | ConvertFrom-Json) | Where-Object { $_.current_volume -gt 0 } | Format-Table -Property @{Label='Chapter Key'; Expression={$_.chapter_key}}, @{Label='Questions'; Expression={$_.current_volume}}, @{Label='Subject'; Expression={$_.subject}} -AutoSize"
pause