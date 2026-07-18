#!/bin/bash

set -u

PROJECT="$HOME/Documents/GitHub/istanbul-housing-market-analytics-pipeline"
SCHEDULER_LOG="$PROJECT/logs/scheduler.log"

export PATH="/opt/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export HOME="/Users/rukiyeerdogan"

{
    echo
    echo "========================================"
    echo "Scheduler-Prüfung: $(date)"
    echo "========================================"

    DAY_OF_MONTH=$((10#$(date '+%d')))

    if (( DAY_OF_MONTH % 2 != 0 )); then
        echo "Heute ist Kalendertag $DAY_OF_MONTH."
        echo "Kein Pipeline-Lauf – Ausführung nur an geraden Tagen."
        exit 0
    fi

    echo "Gerader Kalendertag erkannt."
    echo "Pipeline wird gestartet."

    cd "$PROJECT" || {
        echo "❌ Projektordner nicht gefunden: $PROJECT"
        exit 1
    }

    /bin/bash "$PROJECT/run_full_pipeline.sh"

    STATUS=$?

    if [[ $STATUS -eq 0 ]]; then
        echo "✅ Geplanter Pipeline-Lauf erfolgreich beendet."
    else
        echo "❌ Pipeline wurde mit Fehlercode $STATUS beendet."
    fi

    exit "$STATUS"

} >> "$SCHEDULER_LOG" 2>&1
