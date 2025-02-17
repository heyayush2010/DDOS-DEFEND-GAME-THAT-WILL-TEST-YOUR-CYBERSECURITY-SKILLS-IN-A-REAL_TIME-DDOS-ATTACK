import time

print("Welcome to DDOS DEFENDER game. This game will enhance cybersecurity skills. It will let you play the real role of an IP administrator in a DDOS attack. A DDOS attack is when multiple requests are sent to a port/IP address or through a botnet. This is done by the attacker to increase the computer memory/cpu. Eventually, the high memory will cause the computer to crash and lose all data. You have to play the role of trying to reduce the memory/cpu to as low as possible to avoid this. Press enter to reduce the memory/cpu. Enjoy, don't let the computer crash. If the memory is still high within two minutes you've failed.")
input("Press enter to start the game...")

start_time = time.time()
end_time = start_time + 120  # 2 minutes in seconds
press_count = 0
required_presses = 200  # Number of presses required to thwart the attack
cpu_memory_usage = 97  # Initial CPU/memory usage percentage

while time.time() < end_time:
    input("Press Enter to reduce memory/cpu...")
    press_count += 1
    if press_count % 10 == 0:
        cpu_memory_usage -= 1  # Reduce CPU/memory usage by 1% every 10 presses
    print(f"Memory/cpu reduced! Current usage: {cpu_memory_usage}%")

    if press_count >= required_presses:
        print("You have thwarted the DDOS attack! The device has returned back to normal.")
        break

if press_count < required_presses:
    print("Time's up! If the memory/cpu is still high, you've failed.")