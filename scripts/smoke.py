import json, re, time
from pathlib import Path
from genlayer_py import create_account, create_client
from genlayer_py.chains import studionet
from genlayer_py.types import TransactionStatus

R = Path(__file__).parents[1]
env = (R.parents[3] / 'accounts.env').read_text()
address = json.loads((R / 'deployment.json').read_text())['contractAddress']
def account(number):
    key = re.search(rf'^ACCOUNT_{number}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)', env, re.M).group(1).strip()
    return create_account(account_private_key=key)
def client(number): return create_client(chain=studionet, account=account(number))
def write(number, name, args):
    c = client(number); tx = c.write_contract(address=address, function_name=name, args=args); print(name + '_tx=' + str(tx), flush=True)
    receipt = c.wait_for_transaction_receipt(transaction_hash=tx, status=TransactionStatus.FINALIZED, retries=180, interval=5000, full_transaction=True)
    leader = (receipt.get('consensus_data', {}).get('leader_receipt') or [{}])[0]
    assert receipt.get('result_name') == 'MAJORITY_AGREE' and leader.get('execution_result') == 'SUCCESS'
    return str(tx)

stamp = str(int(time.time())); docket_id = 'DISPATCH-' + stamp
sources = ['https://raw.githubusercontent.com/SAMiiNW/interval-docket/58a642ebeb6125ce00bbcd38fbe0160ee0c98c23/evidence/dispatch-log.md','https://cdn.jsdelivr.net/gh/SAMiiNW/interval-docket@58a642ebeb6125ce00bbcd38fbe0160ee0c98c23/evidence/board-minutes.md']
events = ['Notice issued','Operator response received','Approval recorded']
txs = {}
txs['open'] = write(1, 'open_docket', [docket_id, account(2).address, 'Dispatch and approval chronology', events, [[0,1],[1,2]]])
txs['reconstruct'] = write(2, 'reconstruct', [docket_id, sources])
state = client(1).read_contract(address=address, function_name='get_docket', args=[docket_id])
assert state['state'] == 'CONSISTENT' and len(state['intervals']) == 3 and all(len(row) > 0 for row in state['citations'])
proof = {'docketId':docket_id,'transactions':txs,'state':state,'walletDisclosure':'Both wallets and both evidence documents are operator-controlled technical fixtures.'}
(R / 'evidence' / 'live-proof.json').write_text(json.dumps(proof, indent=2) + '\n')
print(json.dumps(proof, indent=2), flush=True)
