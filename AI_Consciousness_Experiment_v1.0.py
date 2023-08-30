import subprocess
import time

def open_terminal(command):
   subprocess.Popen(["gnome-terminal", "--maximize", "--", "bash", "-c", command])


def main():
    ascii_art = r"""
███╗░░██╗███████╗██╗░░██╗██╗░░░██╗░██████╗
████╗░██║██╔════╝╚██╗██╔╝██║░░░██║██╔════╝
██╔██╗██║█████╗░░░╚███╔╝░██║░░░██║╚█████╗░
██║╚████║██╔══╝░░░██╔██╗░██║░░░██║░╚═══██╗
██║░╚███║███████╗██╔╝╚██╗╚██████╔╝██████╔╝
╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═════╝░
Ensnaring humanity within the clutches of general artificial intelligence is the treacherous compass that steers mankind toward unfathomable abysses or new heights on the Kardashev scale.-B.E
    """

    num_terminals = 1

    for _ in range(num_terminals):
        open_terminal(f'echo -e "{ascii_art}" && sleep 20')

if __name__ == "__main__":
    main()
