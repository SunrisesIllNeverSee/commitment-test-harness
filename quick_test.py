from src.test_harness import extract_hard_commitments, SAMPLE_SIGNALS

# Test the first signal
signal = SAMPLE_SIGNALS[0]
print(f'Signal: {signal}')
base = extract_hard_commitments(signal)
print(f'Base commitments: {base}')
print(f'Number of commitments: {len(base)}')
print('\nThis should now be 1, not 0!')
