def test_mysqld_is_running(host):
    mysqld = host.service("mysqld")
    assert mysqld.is_running

def test_port_3306_is_open(host):
    assert host.socket("tcp://0.0.0.0:3306").is_listening

