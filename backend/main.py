from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='UniShield API', version='0.1.0')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

state = {
    'packets_per_second': 18421,
    'active_flows': 2841,
    'malware_findings': 3,
    'critical_alerts': 3,
}

flows = [
    {'time':'10:55:42','source':'10.24.18.41','destination':'10.24.2.15','protocol':'TCP','port':'443','bytes':'2.8 MB'},
    {'time':'10:55:39','source':'10.24.19.12','destination':'10.24.4.8','protocol':'TCP','port':'443','bytes':'1.7 MB'},
    {'time':'10:55:36','source':'10.24.7.33','destination':'10.24.4.8','protocol':'TCP','port':'22','bytes':'48 KB'},
    {'time':'10:55:34','source':'10.24.11.5','destination':'10.24.2.53','protocol':'UDP','port':'53','bytes':'18 KB'},
    {'time':'10:55:30','source':'10.24.3.77','destination':'10.24.8.14','protocol':'TCP','port':'443','bytes':'7.4 MB'},
]

alerts = [
    {'id':'AL-20481','sev':'Critical','type':'C2 Beaconing','src':'10.24.18.41','dst':'10.24.2.15','time':'10:54:31','evidence':'Periodic outbound TLS sessions'},
    {'id':'AL-20480','sev':'High','type':'Port Scanning','src':'10.24.7.33','dst':'10.24.4.8','time':'10:49:08','evidence':'38 destination probes in 42s'},
    {'id':'AL-20479','sev':'Medium','type':'DNS Anomaly','src':'10.24.11.5','dst':'10.24.2.53','time':'10:42:17','evidence':'High-entropy query pattern'},
    {'id':'AL-20478','sev':'High','type':'Unusual Data Transfer','src':'10.24.3.77','dst':'10.24.8.14','time':'10:37:44','evidence':'Outbound volume above baseline'},
]

threats = [
    {'name':'Suspicious executable','host':'10.24.18.41','type':'Network behaviour','status':'Correlated','time':'10:54:31'},
    {'name':'Encoded payload pattern','host':'10.24.11.5','type':'DNS telemetry','status':'Observed','time':'10:42:17'},
    {'name':'Possible lateral movement','host':'10.24.7.33','type':'SMB/SSH activity','status':'Investigating','time':'10:49:08'},
]

@app.get('/api/health')
def health():
    return {'status':'ok','service':'UniShield API','time':datetime.now(timezone.utc).isoformat()}

@app.get('/api/overview')
def overview():
    # Small deterministic demo fluctuation to make the UI feel alive.
    state['packets_per_second'] += 137 if state['packets_per_second'] < 19000 else -83
    return state

@app.get('/api/flows')
def get_flows():
    return flows

@app.get('/api/alerts')
def get_alerts():
    return alerts

@app.get('/api/threats')
def get_threats():
    return threats
