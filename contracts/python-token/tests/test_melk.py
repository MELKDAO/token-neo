project_root_folder = '/home/lorenzobattistela/Code/melk-token/melk-token/neo/'
PATH = f'{project_root_folder}/contracts/melk.nef'

def test_decimals(neo_test_runner):
    invoke = neo_test_runner.call_contract(PATH, 'decimals')
    neo_test_runner.execute()
    assert invoke.result == 18


def test_symbol(neo_test_runner):
    invoke = neo_test_runner.call_contract(PATH, 'symbol')
    neo_test_runner.execute()
    assert invoke.result == 'MELK'

def test_is_paused(neo_test_runner):
    invoke = neo_test_runner.call_contract(PATH, 'is_paused')
    neo_test_runner.execute()
    assert invoke.result == False

def test_total_supply(neo_test_runner):
    invoke = neo_test_runner.call_contract(PATH, 'totalSupply')
    neo_test_runner.execute()
    assert invoke.result == 10_000_000 * 10 ** 18
