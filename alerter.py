alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 500 for a failure case simulation
    if celcius > 200:
        return 500
    return 200

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 1  # Fix the bug, should increment by 1 on failure

# Strengthening test cases with failure simulation
alert_in_celcius(400.5)  # Should trigger a failure (returns 500)
alert_in_celcius(303.6)  # Should be OK (returns 200)
assert(alert_failure_count == 1)  # Should fail because the count isn't correctly updated

# Test environment using the stub
alert_in_celcius(400.5, network_alert_stub)  # Should trigger a failure
alert_in_celcius(303.6, network_alert_stub)  # Should be OK

print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
