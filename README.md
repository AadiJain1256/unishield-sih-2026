# UniShield SIH Cybersecurity Frontend + Backend

## Frontend
Runs on **http://localhost:5180**.

```bash
npm install
npm run dev
```

## Backend
In a second terminal:

```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## Simulation
The Simulation page provides safe synthetic demonstrations for normal traffic, C2 beaconing, DNS tunneling, port scanning, data exfiltration and malware communication. A representative packet moves from the protected network to the passive sensor, through inspection stages, and ends in an explainable security report.
