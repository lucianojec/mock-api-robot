*** Settings ***
Library    RequestsLibrary
Library    Process

*** Test Cases ***
Testar API com Mock Dinâmico
    [Setup]     Iniciar Mock
    Criar Sessão de Teste
    Validar Endpoint
    [Teardown]  Finalizar Mock

*** Keywords ***
Iniciar Mock
    
    Start Process    python    mock_server.py    stdout=mock.log    stderr=mock.err    shell=True

    Run Process      python    wait_for_port.py    8888

Finalizar Mock
    Run Process    python    stop_mock_server.py

Criar Sessão de Teste
    Create Session    mock    http://localhost:8888

Validar Endpoint
    ${resp}=    GET On Session    mock    /api/teste
    Should Be Equal As Strings    ${resp.status_code}    200
    Should Contain    ${resp.text}    Mock funcionando
