# module2_data.py
# Comprehensive question items for Module 2: Basic Switch and End Device Configuration (ITN v7.0)

MODULE_2_ITEMS = [
    # 2.1 Cisco IOS Access - Operating Systems & GUI/CLI
    {
        "q": "The user interface of an operating system that allows users to request specific tasks through either CLI or GUI interfaces is called the ____.",
        "a": "shell",
        "distractors": ["kernel", "hardware", "firmware"],
        "topic": "2.1 Operating Systems",
        "explanation": "The shell is the user interface that allows users to request specific tasks from the computer via CLI or GUI."
    },
    {
        "q": "The core component of an operating system that communicates directly between computer hardware and software to manage hardware resources is the ____.",
        "a": "kernel",
        "distractors": ["shell", "BIOS", "registry"],
        "topic": "2.1 Operating Systems",
        "explanation": "The kernel communicates between the hardware and software of a computer and manages how resources are used."
    },
    {
        "q": "The physical parts and underlying electronic circuitry of a computer or network device are collectively known as the ____.",
        "a": "hardware",
        "distractors": ["software", "middleware", "firmware"],
        "topic": "2.1 Operating Systems",
        "explanation": "Hardware represents the physical parts of a computer including underlying electronics."
    },
    {
        "q": "A user-friendly operating system interface that allows users to interact with a system using graphical icons, menus, and windows is a ____.",
        "a": "GUI (Graphical User Interface)",
        "distractors": ["CLI (Command Line Interface)", "API", "Kernel shell"],
        "topic": "2.1 GUI",
        "explanation": "A GUI allows the user to interact with the system using graphical icons, menus, and windows."
    },
    {
        "q": "Network operating systems on infrastructure devices like switches and routers are typically accessed and configured through a text-based ____.",
        "a": "CLI (Command Line Interface)",
        "distractors": ["GUI", "touchscreen", "web wizard only"],
        "topic": "2.1 GUI",
        "explanation": "Network devices are typically accessed through a CLI because GUIs can crash, fail, or consume unnecessary resources."
    },
    {
        "q": "One reason network devices rely primarily on a CLI rather than a GUI is because GUIs consume extra resources and can fail, freeze, or ____.",
        "a": "crash",
        "distractors": ["encrypt", "re-route", "authenticate"],
        "topic": "2.1 GUI",
        "explanation": "GUIs can fail, crash, or simply not operate as specified; network devices are typically accessed through CLI."
    },
    {
        "q": "While a PC operating system enables users to use a mouse and view visual output, a CLI-based network operating system relies primarily on a technician using a ____.",
        "a": "keyboard",
        "distractors": ["touchpad", "stylus pen", "graphics tablet"],
        "topic": "2.1 Purpose of an OS",
        "explanation": "A CLI-based network OS enables a network technician to use a keyboard to run CLI-based network programs and enter text commands."
    },

    # 2.1 Cisco IOS Access - Access Methods
    {
        "q": "A physical management port on a Cisco network device used for out-of-band maintenance and initial device configuration is the ____.",
        "a": "console port",
        "distractors": ["Ethernet port", "VTY line", "AUX port"],
        "topic": "2.1 Access Methods",
        "explanation": "The console port is a physical management port used to access a device for maintenance, such as initial configuration."
    },
    {
        "q": "The recommended method for remotely and securely connecting to the CLI of a Cisco device over a network is ____.",
        "a": "Secure Shell (SSH)",
        "distractors": ["Telnet", "TFTP", "HTTP"],
        "topic": "2.1 Access Methods",
        "explanation": "SSH establishes a secure remote CLI connection through a virtual interface over a network with encryption."
    },
    {
        "q": "An older remote terminal protocol that establishes a remote CLI connection over the network but transmits passwords and data in plaintext is ____.",
        "a": "Telnet",
        "distractors": ["SSH", "HTTPS", "SFTP"],
        "topic": "2.1 Access Methods",
        "explanation": "Telnet establishes an insecure remote CLI connection where user authentication, passwords, and commands are sent in plaintext."
    },
    {
        "q": "Connecting to a network device via the console port is considered an out-of-band management method because it does not require active ____.",
        "a": "network services",
        "distractors": ["electrical power", "a serial cable", "terminal software"],
        "topic": "2.1 Access Methods",
        "explanation": "Console access does not require any network connectivity or IP configuration on the device."
    },
    {
        "q": "Software applications such as PuTTY, Tera Term, and SecureCRT used by technicians to connect to network devices are known as ____.",
        "a": "terminal emulation programs",
        "distractors": ["packet analyzers", "compilers", "debuggers"],
        "topic": "2.1 Terminal Emulation Programs",
        "explanation": "Terminal emulation programs are used to connect to a network device by either a console port or SSH/Telnet."
    },

    # 2.2 IOS Navigation - Command Modes
    {
        "q": "The basic Cisco IOS command mode that allows access to only a limited number of basic monitoring commands is called ____.",
        "a": "User EXEC mode",
        "distractors": ["Privileged EXEC mode", "Global configuration mode", "Line configuration mode"],
        "topic": "2.2 Primary Command Modes",
        "explanation": "User EXEC mode allows access to only a limited number of basic monitoring commands."
    },
    {
        "q": "On a Cisco IOS device named Switch, the User EXEC mode is identified by the prompt symbol ending with ____.",
        "a": ">",
        "distractors": ["#", "$", "%"],
        "topic": "2.2 Primary Command Modes",
        "explanation": "User EXEC mode is identified by the CLI prompt that ends with the > symbol (e.g., Switch>)."
    },
    {
        "q": "The Cisco IOS command mode that allows access to all device commands, monitoring features, and configuration modes is ____.",
        "a": "Privileged EXEC mode",
        "distractors": ["User EXEC mode", "Interface mode", "Setup mode"],
        "topic": "2.2 Primary Command Modes",
        "explanation": "Privileged EXEC mode allows access to all commands and features and is identified by the # prompt."
    },
    {
        "q": "On a Cisco IOS device named Switch, the Privileged EXEC mode is identified by the prompt ending with ____.",
        "a": "#",
        "distractors": [">", ":", "~"],
        "topic": "2.2 Primary Command Modes",
        "explanation": "Privileged EXEC mode is identified by the CLI prompt ending with the # symbol (e.g., Switch#)."
    },
    {
        "q": "The primary configuration mode used to configure device-wide settings and access specific subconfiguration modes is called ____.",
        "a": "global configuration mode",
        "distractors": ["interface configuration mode", "line configuration mode", "user EXEC mode"],
        "topic": "2.2 Configuration Modes",
        "explanation": "Global configuration mode is used to access configuration options on the device."
    },
    {
        "q": "The CLI prompt displayed when entering global configuration mode on a switch named Switch is ____.",
        "a": "Switch(config)#",
        "distractors": ["Switch(config-line)#", "Switch(config-if)#", "Switch#"],
        "topic": "2.2 Configuration Modes",
        "explanation": "Global configuration mode is designated by the prompt Switch(config)#."
    },
    {
        "q": "The subconfiguration mode used to configure console, AUX, SSH, or Telnet access lines is called ____.",
        "a": "line configuration mode",
        "distractors": ["interface configuration mode", "vlan configuration mode", "routing configuration mode"],
        "topic": "2.2 Subconfiguration Modes",
        "explanation": "Line configuration mode is used to configure console, SSH, Telnet or AUX access."
    },
    {
        "q": "The CLI prompt displayed when configuring a console or VTY line on a switch is ____.",
        "a": "Switch(config-line)#",
        "distractors": ["Switch(config-if)#", "Switch(config)#", "Switch>"],
        "topic": "2.2 Subconfiguration Modes",
        "explanation": "Line configuration mode displays the prompt Switch(config-line)#."
    },
    {
        "q": "The subconfiguration mode used to configure a switch port or router physical interface is called ____.",
        "a": "interface configuration mode",
        "distractors": ["line configuration mode", "device configuration mode", "system configuration mode"],
        "topic": "2.2 Subconfiguration Modes",
        "explanation": "Interface configuration mode is used to configure a switch port or router interface."
    },
    {
        "q": "The CLI prompt displayed when configuring a switch interface such as FastEthernet or VLAN 1 is ____.",
        "a": "Switch(config-if)#",
        "distractors": ["Switch(config-line)#", "Switch(config)#", "Switch#"],
        "topic": "2.2 Subconfiguration Modes",
        "explanation": "Interface configuration mode displays the prompt Switch(config-if)#."
    },

    # 2.2 IOS Navigation - Navigation Commands
    {
        "q": "To move from User EXEC mode to Privileged EXEC mode, the administrator enters the command ____.",
        "a": "enable",
        "distractors": ["disable", "configure terminal", "exit"],
        "topic": "2.2 Navigation Between Modes",
        "explanation": "The enable command transitions the CLI from User EXEC mode to Privileged EXEC mode."
    },
    {
        "q": "To move from Privileged EXEC mode down to User EXEC mode, enter the command ____.",
        "a": "disable",
        "distractors": ["enable", "exit", "logout"],
        "topic": "2.2 Navigation Between Modes",
        "explanation": "The disable command returns the CLI from Privileged EXEC mode to User EXEC mode."
    },
    {
        "q": "To navigate from Privileged EXEC mode into global configuration mode, execute the command ____.",
        "a": "configure terminal",
        "distractors": ["enable config", "setup terminal", "interface config"],
        "topic": "2.2 Navigation Between Modes",
        "explanation": "The configure terminal command moves the device from Privileged EXEC into global configuration mode."
    },
    {
        "q": "To return from global configuration mode back to Privileged EXEC mode, or from any subconfiguration mode back to global configuration mode, use the command ____.",
        "a": "exit",
        "distractors": ["quit", "stop", "back"],
        "topic": "2.2 Navigation Between Modes",
        "explanation": "The exit command returns to the immediately preceding command mode."
    },
    {
        "q": "To exit from any subconfiguration mode directly back to Privileged EXEC mode in a single step, use the command ____.",
        "a": "end",
        "distractors": ["exit", "return", "close"],
        "topic": "2.2 Navigation Between Modes",
        "explanation": "The end command returns directly to Privileged EXEC mode from any configuration mode."
    },
    {
        "q": "The keyboard shortcut that performs the exact same function as the 'end' command by returning directly to Privileged EXEC mode is ____.",
        "a": "Ctrl+Z",
        "distractors": ["Ctrl+C", "Ctrl+X", "Ctrl+Shift+6"],
        "topic": "2.2 Navigation Between Modes",
        "explanation": "The key combination Ctrl+Z ends any configuration mode and returns to privileged EXEC mode."
    },

    # 2.3 The Command Structure - Syntax Conventions
    {
        "q": "In a Cisco IOS command string, a predefined parameter defined by the operating system is known as a ____.",
        "a": "keyword",
        "distractors": ["argument", "variable", "constant"],
        "topic": "2.3 Basic IOS Command Structure",
        "explanation": "A keyword is a specific parameter defined in the operating system (e.g., 'ip protocols')."
    },
    {
        "q": "In a Cisco IOS command string, a user-supplied parameter or variable (such as an IP address or password) is called an ____.",
        "a": "argument",
        "distractors": ["keyword", "operand", "delimiter"],
        "topic": "2.3 Basic IOS Command Structure",
        "explanation": "An argument is not predefined; it is a value or variable defined by the user (e.g., '192.168.10.5')."
    },
    {
        "q": "In Cisco IOS command syntax documentation, text formatted in boldface indicates commands and keywords that must be entered ____.",
        "a": "literally as shown",
        "distractors": ["in uppercase only", "as user-defined variables", "as optional values"],
        "topic": "2.3 IOS Command Syntax Check",
        "explanation": "Boldface text indicates commands and keywords that you enter literally as shown."
    },
    {
        "q": "In Cisco IOS command syntax documentation, text formatted in italics indicates an element for which the user must supply a ____.",
        "a": "value",
        "distractors": ["literal string", "bracket", "command prompt"],
        "topic": "2.3 IOS Command Syntax Check",
        "explanation": "Italic text indicates arguments for which you supply values."
    },
    {
        "q": "In Cisco command syntax conventions, elements enclosed within square brackets [ ] represent an ____ element.",
        "a": "optional",
        "distractors": ["mandatory", "required", "obsolete"],
        "topic": "2.3 IOS Command Syntax Check",
        "explanation": "Square brackets [x] indicate an optional element (keyword or argument)."
    },
    {
        "q": "In Cisco command syntax conventions, elements enclosed within braces { } represent a ____ element.",
        "a": "required",
        "distractors": ["optional", "deprecated", "commented"],
        "topic": "2.3 IOS Command Syntax Check",
        "explanation": "Braces {x} indicate a required element (keyword or argument)."
    },
    {
        "q": "In Cisco command syntax conventions, a vertical line | within braces or brackets represents a ____.",
        "a": "choice between mutually exclusive elements",
        "distractors": ["pipe to file output", "wildcard character", "logical AND condition"],
        "topic": "2.3 IOS Command Syntax Check",
        "explanation": "A vertical line | indicates a required or optional choice between mutually exclusive elements."
    },
    {
        "q": "In Cisco syntax conventions, the pattern [x {y | z}] indicates a required choice within an ____ element.",
        "a": "optional",
        "distractors": ["mandatory", "encrypted", "administrative"],
        "topic": "2.3 IOS Command Syntax Check",
        "explanation": "Braces and vertical lines within square brackets indicate a required choice within an optional element."
    },
    {
        "q": "The Cisco IOS command used to verify layer 3 IP reachability to a destination device by sending ICMP echo requests is ____.",
        "a": "ping",
        "distractors": ["traceroute", "telnet", "arp"],
        "topic": "2.3 IOS Command Syntax Check",
        "explanation": "The ping command sends ICMP echo requests to test connectivity to an IP address."
    },
    {
        "q": "The Cisco IOS command used to trace the path and display intermediate router hops to a remote host is ____.",
        "a": "traceroute",
        "distractors": ["ping", "netstat", "ipconfig"],
        "topic": "2.3 IOS Command Syntax Check",
        "explanation": "The traceroute command traces the route and lists each intermediate router hop to a destination."
    },

    # 2.3 Command Structure - Help Features & Shortcuts
    {
        "q": "Entering a question mark (?) at the CLI prompt to see which commands or arguments are available utilizes the feature called ____.",
        "a": "context-sensitive help",
        "distractors": ["command syntax check", "terminal logging", "auto-complete buffer"],
        "topic": "2.3 IOS Help Features",
        "explanation": "Context-sensitive help allows users to see available commands, keywords, and arguments by typing '?'."
    },
    {
        "q": "When an entered command is incomplete, ambiguous, or invalid, the IOS feature that provides feedback indicating the error is ____.",
        "a": "command syntax check",
        "distractors": ["context-sensitive help", "terminal history", "packet checker"],
        "topic": "2.3 IOS Help Features",
        "explanation": "Command syntax check verifies that a valid command was entered and gives feedback if invalid."
    },
    {
        "q": "In the Cisco CLI, entering a unique starting sequence of characters and pressing the ____ key will automatically complete the command.",
        "a": "Tab",
        "distractors": ["Spacebar", "Enter", "Esc"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "The Tab key completes a partial command name entry."
    },
    {
        "q": "In the Cisco CLI, commands can be shortened to the minimum number of characters that identify a ____ selection.",
        "a": "unique",
        "distractors": ["numerical", "alphabetic", "case-sensitive"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "Commands and keywords can be shortened to the minimum number of characters that identify a unique selection."
    },
    {
        "q": "The keystroke used in the CLI editing buffer to erase the character to the left of the cursor is ____.",
        "a": "Backspace",
        "distractors": ["Delete", "Spacebar", "Tab"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "Backspace erases the character to the left of the cursor."
    },
    {
        "q": "The keyboard shortcut that moves the cursor one character to the left, identical to the Left Arrow key, is ____.",
        "a": "Ctrl+B",
        "distractors": ["Ctrl+F", "Ctrl+P", "Ctrl+A"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "Left Arrow or Ctrl+B moves the cursor one character to the left."
    },
    {
        "q": "The keyboard shortcut that moves the cursor one character to the right, identical to the Right Arrow key, is ____.",
        "a": "Ctrl+F",
        "distractors": ["Ctrl+B", "Ctrl+N", "Ctrl+E"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "Right Arrow or Ctrl+F moves the cursor one character to the right."
    },
    {
        "q": "The keyboard shortcut that recalls the previous command in the history buffer, identical to the Up Arrow key, is ____.",
        "a": "Ctrl+P",
        "distractors": ["Ctrl+N", "Ctrl+U", "Ctrl+R"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "Up Arrow or Ctrl+P recalls commands in the history buffer, beginning with the most recent."
    },
    {
        "q": "When command output produces more text than can be displayed in the terminal window, the IOS pauses and displays the ____ prompt.",
        "a": "--More--",
        "distractors": ["--Continue--", "--Wait--", "--Pause--"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "When output exceeds the terminal window, the IOS displays a '--More--' prompt."
    },
    {
        "q": "While viewing output at the '--More--' prompt, pressing the ____ displays the next single line.",
        "a": "Enter key",
        "distractors": ["Spacebar", "Tab key", "Shift key"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "At the '--More--' prompt, the Enter key displays the next line."
    },
    {
        "q": "While viewing output at the '--More--' prompt, pressing the ____ displays the next full screen.",
        "a": "Spacebar",
        "distractors": ["Enter key", "Tab key", "Backspace"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "At the '--More--' prompt, the Spacebar displays the next full screen."
    },
    {
        "q": "Pressing any alphanumeric key other than Enter or Spacebar while at the '--More--' prompt ends the display string and returns to ____.",
        "a": "Privileged EXEC mode",
        "distractors": ["User EXEC mode", "Global configuration mode", "ROMmon mode"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "Pressing any other key ends the display string, returning to privileged EXEC mode."
    },
    {
        "q": "When in any configuration mode, entering the shortcut ____ ends configuration mode and returns to privileged EXEC mode.",
        "a": "Ctrl-C",
        "distractors": ["Ctrl-D", "Ctrl-A", "Ctrl-Shift-6"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "Ctrl-C ends configuration mode and returns to privileged EXEC mode."
    },
    {
        "q": "The all-purpose break sequence used to abort DNS lookups, traceroutes, and pings on Cisco devices is ____.",
        "a": "Ctrl-Shift-6",
        "distractors": ["Ctrl-C", "Ctrl-Z", "Ctrl-Alt-Delete"],
        "topic": "2.3 Hot Keys and Shortcuts",
        "explanation": "Ctrl-Shift-6 is the all-purpose break sequence used to abort DNS lookups, traceroutes, pings, etc."
    },

    # 2.4 Basic Device Configuration - Device Names & Passwords
    {
        "q": "The very first configuration command that should be applied to any Cisco device to provide a unique network identity is assigning a ____.",
        "a": "hostname",
        "distractors": ["IP address", "subnet mask", "banner"],
        "topic": "2.4 Device Names",
        "explanation": "The first configuration command on any device should be to give it a unique hostname."
    },
    {
        "q": "By default, an unconfigured Cisco IOS switch is assigned the factory default hostname of ____.",
        "a": "Switch",
        "distractors": ["Router", "Cisco", "Default"],
        "topic": "2.4 Device Names",
        "explanation": "By default, all Cisco IOS switches are assigned the factory default name 'Switch'."
    },
    {
        "q": "According to Cisco naming guidelines, a device hostname must start with a letter, contain no spaces, end with a letter or digit, and be less than ____ characters in length.",
        "a": "64",
        "distractors": ["32", "128", "256"],
        "topic": "2.4 Device Names",
        "explanation": "Hostnames must start with a letter, have no spaces, end with letter/digit, and be less than 64 characters."
    },
    {
        "q": "To remove a configured hostname and return a switch prompt to its factory default name, enter the global command ____.",
        "a": "no hostname",
        "distractors": ["clear hostname", "erase hostname", "default hostname"],
        "topic": "2.4 Device Names",
        "explanation": "To return the switch to the default prompt, use the 'no hostname' global config command."
    },
    {
        "q": "Cisco password guidelines recommend that passwords used for administrative device security should be more than ____ characters in length.",
        "a": "eight",
        "distractors": ["four", "six", "sixteen"],
        "topic": "2.4 Password Guidelines",
        "explanation": "Cisco recommends passwords that are more than eight characters in length."
    },
    {
        "q": "Simple passwords such as 'cisco' or 'class' used in lab environments are considered weak and easily guessable, and should be avoided in ____ environments.",
        "a": "production",
        "distractors": ["simulation", "virtual", "classroom"],
        "topic": "2.4 Password Guidelines",
        "explanation": "Simple passwords like 'cisco' or 'class' are weak and should be avoided in production environments."
    },
    {
        "q": "To configure user EXEC password security for the physical management console, the administrator enters the global command ____.",
        "a": "line console 0",
        "distractors": ["line vty 0", "line aux 0", "line terminal 0"],
        "topic": "2.4 Configure Passwords",
        "explanation": "To secure user EXEC mode access via console, first enter line console 0 configuration mode."
    },
    {
        "q": "In line configuration mode, after entering the 'password <string>' command, user EXEC access must be enabled using the command ____.",
        "a": "login",
        "distractors": ["enable", "activate", "auth"],
        "topic": "2.4 Configure Passwords",
        "explanation": "The 'login' command enables password checking upon connecting to the line."
    },
    {
        "q": "To secure Privileged EXEC mode access with an encrypted, hashed password, the administrator uses the global command ____.",
        "a": "enable secret",
        "distractors": ["enable password", "service password", "encrypt enable"],
        "topic": "2.4 Configure Passwords",
        "explanation": "The 'enable secret password' command provides encrypted password protection for privileged EXEC mode."
    },
    {
        "q": "Virtual lines that allow remote administrative access using Telnet or SSH to a Cisco device are called ____ lines.",
        "a": "VTY",
        "distractors": ["AUX", "Console", "Ethernet"],
        "topic": "2.4 Configure Passwords",
        "explanation": "VTY (Virtual Terminal) lines enable remote access using Telnet or SSH to the device."
    },
    {
        "q": "Many Cisco switches support up to 16 virtual terminal lines, which are configured concurrently using the command ____.",
        "a": "line vty 0 15",
        "distractors": ["line vty 1 16", "line remote 0 15", "line console 0 15"],
        "topic": "2.4 Configure Passwords",
        "explanation": "Switches support 16 VTY lines numbered 0 to 15, entered using 'line vty 0 15'."
    },

    # 2.4 Basic Device Configuration - Password Encryption & Banners
    {
        "q": "By default, configuration files such as startup-config and running-config display configured passwords in ____.",
        "a": "plaintext",
        "distractors": ["MD5 hashes", "SHA-256 ciphertext", "hexadecimal codes"],
        "topic": "2.4 Encrypt Passwords",
        "explanation": "The startup-config and running-config files display most passwords in plaintext by default."
    },
    {
        "q": "To encrypt all plaintext passwords stored in the configuration files, execute the global configuration command ____.",
        "a": "service password-encryption",
        "distractors": ["encrypt-passwords all", "secure passwords enable", "crypto password-encrypt"],
        "topic": "2.4 Encrypt Passwords",
        "explanation": "The 'service password-encryption' command prevents passwords from appearing as plaintext in config files."
    },
    {
        "q": "To verify that all configured passwords on the device are now encrypted, the administrator executes the Privileged EXEC command ____.",
        "a": "show running-config",
        "distractors": ["show passwords", "show security-keys", "show encryption"],
        "topic": "2.4 Encrypt Passwords",
        "explanation": "Use 'show running-config' to verify that passwords in the active configuration are encrypted."
    },
    {
        "q": "A legal notification displayed to warn unauthorized personnel against attempting to access a device is configured using the global command ____.",
        "a": "banner motd",
        "distractors": ["login prompt", "legal notice", "syslog warning"],
        "topic": "2.4 Banner Messages",
        "explanation": "A banner message of the day is configured using 'banner motd # message #' to warn unauthorized users."
    },
    {
        "q": "In the command 'banner motd # Unauthorized Access Prohibited #', the '#' character placed at the beginning and end of the message is called the ____ character.",
        "a": "delimiting",
        "distractors": ["escape", "control", "wildcard"],
        "topic": "2.4 Banner Messages",
        "explanation": "The character entered before and after the banner message is called the delimiting character."
    },

    # 2.5 Save Configurations - Configuration Files & Storage
    {
        "q": "The saved configuration file stored in NVRAM that is loaded and executed when a Cisco device reboots is called ____.",
        "a": "startup-config",
        "distractors": ["running-config", "boot-config", "active-config"],
        "topic": "2.5 Configuration Files",
        "explanation": "The startup-config is stored in NVRAM and contains commands executed upon reboot."
    },
    {
        "q": "The active configuration file stored in Random Access Memory (RAM) that immediately reflects changes made on the CLI is the ____.",
        "a": "running-config",
        "distractors": ["startup-config", "nvram-config", "flash-config"],
        "topic": "2.5 Configuration Files",
        "explanation": "The running-config is stored in RAM and reflects the current, active device configuration."
    },
    {
        "q": "Because system RAM is ____ memory, modifying the running configuration affects operation immediately, but changes are lost if power is lost.",
        "a": "volatile",
        "distractors": ["non-volatile", "static", "permanent"],
        "topic": "2.5 Configuration Files",
        "explanation": "RAM is volatile memory; it loses all of its contents when the device is powered off or restarted."
    },
    {
        "q": "The persistent storage location where the startup configuration file is preserved across reboots and power outages is ____.",
        "a": "NVRAM",
        "distractors": ["RAM", "ROM cache", "TFTP server"],
        "topic": "2.5 Configuration Files",
        "explanation": "NVRAM (Non-Volatile RAM) does not lose its contents when the device is powered off."
    },
    {
        "q": "To save all active modifications from volatile RAM to non-volatile NVRAM, enter the Privileged EXEC command ____.",
        "a": "copy running-config startup-config",
        "distractors": ["save running-config startup-config", "write ram nvram", "commit startup-config"],
        "topic": "2.5 Configuration Files",
        "explanation": "The 'copy running-config startup-config' command saves the running configuration to NVRAM."
    },
    {
        "q": "If undesirable changes have been made to the running configuration and have not yet been saved, the administrator can restore the previous saved configuration using the command ____.",
        "a": "reload",
        "distractors": ["reboot system", "reset factory", "rollback"],
        "topic": "2.5 Alter the Running Configurations",
        "explanation": "Issuing 'reload' in Privileged EXEC mode reboots the device and reloads startup-config from NVRAM."
    },
    {
        "q": "If unwanted configuration changes have already been saved to the startup configuration file, the administrator can clear NVRAM using the command ____.",
        "a": "erase startup-config",
        "distractors": ["delete running-config", "clear nvram-all", "reset startup-config"],
        "topic": "2.5 Alter the Running Configurations",
        "explanation": "The 'erase startup-config' command clears the saved configuration file from NVRAM."
    },
    {
        "q": "After clearing the startup configuration file from NVRAM with 'erase startup-config', the administrator must enter the ____ command to clear the running-config from RAM.",
        "a": "reload",
        "distractors": ["exit", "shutdown", "erase running-config"],
        "topic": "2.5 Alter the Running Configurations",
        "explanation": "After erasing startup-config, reloading the device clears the running-config from RAM."
    },

    # 2.5 Save Configurations - Capturing Configuration to Text File
    {
        "q": "When archiving a Cisco device configuration to a text file using terminal software such as PuTTY or Tera Term, the first step is to enable session ____.",
        "a": "logging",
        "distractors": ["sniffing", "mirroring", "scripting"],
        "topic": "2.5 Capture Configuration to a Text File",
        "explanation": "Step 2 in capturing config is to enable session logging in the terminal emulation software."
    },
    {
        "q": "While session logging is active in terminal software, the administrator captures the active configuration by issuing the Privileged EXEC command 'show running-config' or ____.",
        "a": "show startup-config",
        "distractors": ["show interfaces", "show flash", "show memory"],
        "topic": "2.5 Capture Configuration to a Text File",
        "explanation": "Executing 'show running-config' or 'show startup-config' prints the configuration into the log file."
    },
    {
        "q": "After capturing configuration output in terminal software, logging is turned off by choosing the session logging option ____.",
        "a": "None",
        "distractors": ["Stop", "Close", "Disable"],
        "topic": "2.5 Capture Configuration to a Text File",
        "explanation": "Session logging is disabled in PuTTY by choosing the 'None' session logging option."
    },

    # 2.6 Ports and Addresses - IP Addresses & Media
    {
        "q": "The primary means of enabling devices to locate one another and establish end-to-end communication on the Internet is using ____.",
        "a": "IP addresses",
        "distractors": ["MAC addresses only", "hostnames only", "port numbers only"],
        "topic": "2.6 IP Addresses",
        "explanation": "IP addresses are the primary means enabling devices to locate one another and establish communication."
    },
    {
        "q": "The structure of an IPv4 address is formatted as four decimal numbers between 0 and 255 separated by dots, known as ____.",
        "a": "dotted decimal notation",
        "distractors": ["hexadecimal notation", "colon-hex format", "binary octet notation"],
        "topic": "2.6 IP Addresses",
        "explanation": "The structure of an IPv4 address is called dotted decimal notation."
    },
    {
        "q": "In an IPv4 address, each of the four decimal numbers must have a value between 0 and ____.",
        "a": "255",
        "distractors": ["127", "256", "512"],
        "topic": "2.6 IP Addresses",
        "explanation": "Each decimal octet in an IPv4 address ranges from 0 to 255."
    },
    {
        "q": "An IPv4 subnet mask is a 32-bit value that differentiates the network portion of the address from the ____ portion.",
        "a": "host",
        "distractors": ["broadcast", "domain", "interface"],
        "topic": "2.6 IP Addresses",
        "explanation": "The subnet mask differentiates the network portion of the address from the host portion."
    },
    {
        "q": "The IP address of the local router interface that an end host uses to reach remote networks and the internet is the ____.",
        "a": "default gateway",
        "distractors": ["subnet mask", "DNS server", "broadcast address"],
        "topic": "2.6 IP Addresses",
        "explanation": "The default gateway is the IP address of the router used by the host to access remote networks."
    },
    {
        "q": "An IPv6 address has a total length of ____ bits.",
        "a": "128",
        "distractors": ["32", "64", "256"],
        "topic": "2.6 IP Addresses",
        "explanation": "IPv6 addresses are 128 bits in length."
    },
    {
        "q": "An IPv6 address is written as a sequence of hexadecimal values separated into groups of four digits by the symbol ____.",
        "a": "colon (:)",
        "distractors": ["period (.)", "hyphen (-)", "slash (/)"],
        "topic": "2.6 IP Addresses",
        "explanation": "Groups of four hexadecimal digits in IPv6 are separated by a colon ':'."
    },
    {
        "q": "In an IPv6 address, each individual hexadecimal digit represents ____ binary bits.",
        "a": "4",
        "distractors": ["8", "16", "32"],
        "topic": "2.6 IP Addresses",
        "explanation": "Every four bits is represented by a single hexadecimal digit."
    },
    {
        "q": "A complete IPv6 address contains a total of ____ hexadecimal digits.",
        "a": "32",
        "distractors": ["16", "64", "128"],
        "topic": "2.6 IP Addresses",
        "explanation": "A 128-bit IPv6 address consists of 32 hexadecimal values (128 / 4 = 32)."
    },
    {
        "q": "Unlike some command parameters, IPv6 addresses are not case-sensitive and can be written in either lowercase or ____.",
        "a": "uppercase",
        "distractors": ["binary", "octal", "italics"],
        "topic": "2.6 IP Addresses",
        "explanation": "IPv6 addresses are not case-sensitive and can be written in lowercase or uppercase."
    },
    {
        "q": "Differences between network media types include transmission speed, cost, environment, and the distance the media can carry a ____.",
        "a": "signal",
        "distractors": ["protocol", "VLAN", "gateway"],
        "topic": "2.6 Interfaces and Ports",
        "explanation": "Differences include distance the media can successfully carry a signal, speed, environment, and cost."
    },

    # 2.7 Configure IP Addressing - Manual & Dynamic IP
    {
        "q": "End devices on a network require an IP address in order to communicate with other devices, which can be configured manually or automatically using ____.",
        "a": "DHCP",
        "distractors": ["DNS", "ARP", "ICMP"],
        "topic": "2.7 Manual IP Address Configuration",
        "explanation": "IPv4 address information can be entered manually or automatically using DHCP."
    },
    {
        "q": "To manually configure an IPv4 address on a Windows PC, a user opens Control Panel > Network Sharing Center > Change adapter settings, selects the adapter, and opens ____ Properties.",
        "a": "Local Area Connection",
        "distractors": ["Administrative Tools", "Device Manager", "Windows Defender"],
        "topic": "2.7 Manual IP Address Configuration",
        "explanation": "Right-clicking the adapter opens the Local Area Connection Properties window."
    },
    {
        "q": "In Windows PC networking, manual IPv4 settings are entered within the Properties dialog of Internet Protocol Version 4 (____).",
        "a": "TCP/IPv4",
        "distractors": ["UDP/IPv4", "ICMP/IPv4", "NETBIOS/IPv4"],
        "topic": "2.7 Manual IP Address Configuration",
        "explanation": "Settings are entered in the Internet Protocol Version 4 (TCP/IPv4) Properties window."
    },
    {
        "q": "The network protocol that automatically assigns an IPv4 address, subnet mask, default gateway, and DNS servers to end devices is ____.",
        "a": "DHCP",
        "distractors": ["DNS", "SMTP", "NTP"],
        "topic": "2.7 Automatic IP Address Configuration",
        "explanation": "DHCP (Dynamic Host Configuration Protocol) enables automatic IPv4 address configuration."
    },
    {
        "q": "By default, end devices such as PCs are configured to obtain an IP address automatically using ____.",
        "a": "DHCP",
        "distractors": ["Static IP", "APIPA only", "Manual assignment"],
        "topic": "2.7 Automatic IP Address Configuration",
        "explanation": "End devices are typically by default using DHCP for automatic IPv4 address configuration."
    },
    {
        "q": "In addition to DHCPv6, an IPv6 end device can automatically acquire dynamic address allocation using ____.",
        "a": "SLAAC (Stateless Address Autoconfiguration)",
        "distractors": ["NAT", "ARP", "Proxy DNS"],
        "topic": "2.7 Automatic IP Address Configuration",
        "explanation": "IPv6 uses DHCPv6 and SLAAC (Stateless Address Autoconfiguration) for dynamic address allocation."
    },

    # 2.7 Switch Virtual Interface (SVI) & Verification
    {
        "q": "To enable remote management access (SSH or Telnet) to a Layer 2 switch across a network, an IP address must be configured on an ____.",
        "a": "SVI (Switch Virtual Interface)",
        "distractors": ["auxiliary line", "console port", "physical loopback cable"],
        "topic": "2.7 Switch Virtual Interface Configuration",
        "explanation": "To access the switch remotely, an IP address and subnet mask must be configured on the SVI."
    },
    {
        "q": "The default Switch Virtual Interface present on Cisco switches used for remote IP management is ____.",
        "a": "interface vlan 1",
        "distractors": ["interface vlan 10", "interface loopback 0", "interface fastethernet 0/1"],
        "topic": "2.7 Switch Virtual Interface Configuration",
        "explanation": "On a Cisco switch, the default virtual management interface is interface vlan 1."
    },
    {
        "q": "To configure an IP address on an SVI, the administrator enters the command 'ip address' followed by the ip-address and the ____.",
        "a": "subnet-mask",
        "distractors": ["default-gateway", "mac-address", "dns-server"],
        "topic": "2.7 Switch Virtual Interface Configuration",
        "explanation": "The syntax is: 'ip address ip-address subnet-mask'."
    },
    {
        "q": "After configuring the IP address and subnet mask on an SVI, the interface must be administratively enabled using the command ____.",
        "a": "no shutdown",
        "distractors": ["enable interface", "start", "up"],
        "topic": "2.7 Switch Virtual Interface Configuration",
        "explanation": "The virtual interface is enabled using the 'no shutdown' interface command."
    },
    {
        "q": "On a Windows PC command prompt, the command used to verify the current IP address, subnet mask, and default gateway configuration is ____.",
        "a": "ipconfig",
        "distractors": ["ifconfig", "show ip", "netstat"],
        "topic": "2.9 Module Practice and Quiz / Commands",
        "explanation": "The 'ipconfig' command displays the IP configuration on a Windows PC."
    },
    {
        "q": "On a Cisco switch CLI, the Privileged EXEC command used to display a concise summary of the status and IP configuration of all interfaces is ____.",
        "a": "show ip interface brief",
        "distractors": ["show interfaces status", "show running-config interface", "show ip route"],
        "topic": "2.9 Module Practice and Quiz / Commands",
        "explanation": "'show ip interface brief' (or 'show ip int brief') lists interfaces, IP addresses, and line status."
    },
    {
        "q": "To navigate from global configuration mode into interface configuration mode for the management VLAN, enter the command ____.",
        "a": "interface vlan 1",
        "distractors": ["line vlan 1", "switchport vlan 1", "interface vlan 0"],
        "topic": "2.7 Switch Virtual Interface Configuration",
        "explanation": "The command 'interface vlan 1' enters SVI configuration mode."
    },
    {
        "q": "The command mode accessed immediately when a user establishes a console connection or boots a Cisco switch without entering passwords is ____.",
        "a": "User EXEC mode",
        "distractors": ["Privileged EXEC mode", "Global configuration mode", "Line configuration mode"],
        "topic": "2.2 Primary Command Modes",
        "explanation": "A user lands in User EXEC mode (prompt '>') upon initial connection."
    }
]
