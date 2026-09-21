# module1_data.py
# Comprehensive question items for Module 1: Networking Today (ITN v7.0)

MODULE_1_ITEMS = [
    # 1.1 Networks Affect Our Lives
    {
        "q": "Modern computer networks enable communication and collaboration across a global scale, creating a world without ____.",
        "a": "boundaries",
        "distractors": ["protocols", "hardware", "delays"],
        "topic": "1.1 Networks Affect Our Lives",
        "explanation": "Networks create a 'world without boundaries' by connecting individuals and communities globally."
    },
    {
        "q": "Advancements in networking technology have allowed people to interact and share ideas in online groups known as global ____.",
        "a": "communities",
        "distractors": ["subnets", "domains", "segments"],
        "topic": "1.1 Networks Affect Our Lives",
        "explanation": "Global communities are formed by individuals sharing common interests across the global network."
    },
    {
        "q": "The global networking platform that supports the way we work, live, play, and learn is referred to by Cisco as the ____ network.",
        "a": "human",
        "distractors": ["converged", "analog", "physical"],
        "topic": "1.1 Networks Affect Our Lives",
        "explanation": "Cisco emphasizes the concept of the 'human network' that enriches human interactions."
    },

    # 1.2 Network Components - Host Roles
    {
        "q": "Every computer connected to a network that participates directly in network communication is classified as a host or ____.",
        "a": "end device",
        "distractors": ["intermediary device", "network medium", "physical interface"],
        "topic": "1.2 Host Roles",
        "explanation": "Hosts or end devices are computers and endpoints that originate or receive data."
    },
    {
        "q": "Computers on a network that provide information, files, or services to other end devices are called ____.",
        "a": "servers",
        "distractors": ["clients", "repeaters", "multiplexers"],
        "topic": "1.2 Host Roles",
        "explanation": "Servers are computers that run specialized software to provide data/services to end devices."
    },
    {
        "q": "Computers that send requests to servers to retrieve information such as web pages, email, or documents are called ____.",
        "a": "clients",
        "distractors": ["hosts of last resort", "gateways", "concentrators"],
        "topic": "1.2 Host Roles",
        "explanation": "Clients run client software that initiates requests to servers to obtain information."
    },
    {
        "q": "A specialized server that runs email server software to manage, send, and store electronic messages is an ____.",
        "a": "email server",
        "distractors": ["FTP server", "proxy firewall", "print server"],
        "topic": "1.2 Host Roles",
        "explanation": "An email server runs email server software while clients use mail clients to access email."
    },
    {
        "q": "To retrieve and display web pages hosted on a web server, clients run client software called a web ____.",
        "a": "browser",
        "distractors": ["terminal emulator", "compiler", "sniffer"],
        "topic": "1.2 Host Roles",
        "explanation": "Clients use browser software to access web pages served by a web server."
    },
    {
        "q": "A dedicated computer on a network that stores corporate and personal files for authorized user access is called a ____.",
        "a": "file server",
        "distractors": ["DNS server", "DHCP relay", "domain gateway"],
        "topic": "1.2 Host Roles",
        "explanation": "A file server stores corporate and user files which client devices access."
    },

    # 1.2 Network Components - Peer-to-Peer
    {
        "q": "A network design where a single computer can act as both a client and a server at the same time is called a ____.",
        "a": "peer-to-peer network",
        "distractors": ["client-server network", "mainframe network", "centralized cloud network"],
        "topic": "1.2 Peer-to-Peer",
        "explanation": "In a peer-to-peer (P2P) network, devices share resources without dedicated centralized servers."
    },
    {
        "q": "An advantage of a peer-to-peer network configuration is that it is less complex, easy to set up, and has a ____.",
        "a": "lower cost",
        "distractors": ["centralized database", "high level of security", "guaranteed throughput"],
        "topic": "1.2 Peer-to-Peer",
        "explanation": "Peer-to-peer advantages include: easy to set up, less complex, and lower cost."
    },
    {
        "q": "A primary disadvantage of implementing a peer-to-peer network is that it has no ____.",
        "a": "centralized administration",
        "distractors": ["IP addressing capability", "copper cable support", "operating system requirement"],
        "topic": "1.2 Peer-to-Peer",
        "explanation": "Peer-to-peer networks have no centralized administration, making security and backups difficult."
    },
    {
        "q": "Peer-to-peer networks are only recommended for very small environments because they are not ____.",
        "a": "scalable",
        "distractors": ["routable", "functional", "digital"],
        "topic": "1.2 Peer-to-Peer",
        "explanation": "P2P networks are not scalable; as more devices are added, performance and administration degrade."
    },
    {
        "q": "Because of security and performance limitations, peer-to-peer networks are typically used only for simple tasks such as transferring files and sharing ____.",
        "a": "printers",
        "distractors": ["routing tables", "encryption certificates", "VLAN configurations"],
        "topic": "1.2 Peer-to-Peer",
        "explanation": "P2P networks are primarily used for simple tasks like sharing files and sharing printers."
    },

    # 1.2 Network Components - End Devices & Intermediary Devices
    {
        "q": "A network device where a message originates from or where it is received is known as an ____.",
        "a": "end device",
        "distractors": ["intermediary device", "boundary router", "core switch"],
        "topic": "1.2 End Devices",
        "explanation": "An end device is where data originates from, flows through the network, and arrives."
    },
    {
        "q": "A device that interconnects end devices and manages data as it flows across the network is called an ____.",
        "a": "intermediary network device",
        "distractors": ["endpoint device", "end-user terminal", "passive transmission line"],
        "topic": "1.2 Intermediary Network Devices",
        "explanation": "Intermediary devices interconnect end devices and direct network traffic."
    },
    {
        "q": "Examples of intermediary network devices include switches, routers, firewalls, and ____.",
        "a": "wireless access points",
        "distractors": ["workstations", "VoIP smartphones", "network printers"],
        "topic": "1.2 Intermediary Network Devices",
        "explanation": "Intermediary devices include switches, wireless access points (APs), routers, and firewalls."
    },
    {
        "q": "One primary management function of an intermediary device as data travels across a network is to regenerate and ____.",
        "a": "retransmit data signals",
        "distractors": ["reboot end hosts", "format hard drives", "modify packet payloads"],
        "topic": "1.2 Intermediary Network Devices",
        "explanation": "Intermediary devices regenerate and retransmit data signals across network segments."
    },
    {
        "q": "Intermediary devices manage data flow by maintaining information about what pathways exist through the ____.",
        "a": "network",
        "distractors": ["system bus", "operating system kernel", "hard drive partition"],
        "topic": "1.2 Intermediary Network Devices",
        "explanation": "Intermediary devices (such as routers) maintain pathway and routing information."
    },
    {
        "q": "When a network link failure or communication disruption occurs, an intermediary device notifies other devices of errors and communication ____.",
        "a": "failures",
        "distractors": ["authorizations", "upgrades", "encapsulations"],
        "topic": "1.2 Intermediary Network Devices",
        "explanation": "Intermediary devices notify other devices of communication errors and link failures."
    },

    # 1.2 Network Components - Network Media
    {
        "q": "Communication across a network is carried through a physical channel which allows messages to travel from source to destination, known as network ____.",
        "a": "media",
        "distractors": ["topologies", "protocols", "architectures"],
        "topic": "1.2 Network Media",
        "explanation": "Network media provides the physical pathway or medium through which messages travel."
    },
    {
        "q": "Network media that uses metal wires within cables transmits information using ____.",
        "a": "electrical impulses",
        "distractors": ["pulses of light", "electromagnetic wave modulation", "infrared frequencies"],
        "topic": "1.2 Network Media",
        "explanation": "Copper cabling (metal wires) encodes and transmits data as electrical impulses."
    },
    {
        "q": "Network media that transmits data using glass or plastic fibers within cables is known as ____.",
        "a": "fiber-optic cable",
        "distractors": ["coaxial cable", "shielded twisted-pair", "powerline wire"],
        "topic": "1.2 Network Media",
        "explanation": "Fiber-optic cables use glass or plastic fibers to transmit data as pulses of light."
    },
    {
        "q": "Fiber-optic cabling conveys information across the network by transmitting pulses of ____.",
        "a": "light",
        "distractors": ["electricity", "sound waves", "static voltage"],
        "topic": "1.2 Network Media",
        "explanation": "Fiber-optic cables transmit data using pulses of light."
    },
    {
        "q": "Network transmission that carries data across the air uses modulation of specific frequencies of ____.",
        "a": "electromagnetic waves",
        "distractors": ["acoustic soundwaves", "ultraviolet radiation", "gamma wavelengths"],
        "topic": "1.2 Network Media",
        "explanation": "Wireless network media transmits signals by modulating electromagnetic wave frequencies."
    },

    # 1.3 Network Representations and Topologies
    {
        "q": "A visual diagram that uses standardized symbols to represent devices and connections within a network is a ____.",
        "a": "topology diagram",
        "distractors": ["schematic blueprint", "flowchart", "logic table"],
        "topic": "1.3 Network Representations",
        "explanation": "Topology diagrams represent network devices and interconnections using standard symbols."
    },
    {
        "q": "A specialized expansion card or onboard chip that physically connects an end device to network media is a ____.",
        "a": "Network Interface Card (NIC)",
        "distractors": ["Central Processing Unit (CPU)", "Default Gateway", "Power Supply Unit (PSU)"],
        "topic": "1.3 Network Representations",
        "explanation": "A Network Interface Card (NIC) connects an end device to the physical network media."
    },
    {
        "q": "A physical connector or outlet on a networking device where media is plugged in to connect to other devices is called a physical ____.",
        "a": "port",
        "distractors": ["socket", "bus", "switchboard"],
        "topic": "1.3 Network Representations",
        "explanation": "A physical port is an outlet/connector on a network device where cables attach."
    },
    {
        "q": "Specialized ports on a networking device that connect directly to individual networks are called ____.",
        "a": "interfaces",
        "distractors": ["patch bays", "transceivers", "repeaters"],
        "topic": "1.3 Network Representations",
        "explanation": "Interfaces are specialized ports on a network device connecting to specific networks."
    },
    {
        "q": "In Cisco networking terminology, the terms 'interface' and '____' are frequently used interchangeably.",
        "a": "port",
        "distractors": ["cable", "bridge", "subnet"],
        "topic": "1.3 Network Representations",
        "explanation": "Cisco notes that often the terms 'port' and 'interface' are used interchangeably."
    },
    {
        "q": "A network diagram that illustrates the physical location of intermediary devices, rack locations, and cable installation is a ____.",
        "a": "physical topology diagram",
        "distractors": ["logical topology diagram", "conceptual data schema", "wiring flowchart"],
        "topic": "1.3 Topology Diagrams",
        "explanation": "Physical topology diagrams show physical locations (rooms, racks) and cable routes."
    },
    {
        "q": "A network diagram that illustrates device names, port designations, and the IP addressing scheme is a ____.",
        "a": "logical topology diagram",
        "distractors": ["physical topology diagram", "structural blueprint", "architectural floor plan"],
        "topic": "1.3 Topology Diagrams",
        "explanation": "Logical topology diagrams illustrate devices, ports, and the addressing scheme of the network."
    },

    # 1.4 Common Types of Networks
    {
        "q": "A network type that connects a few computers to each other and to the internet within a private residence is a ____.",
        "a": "small home network",
        "distractors": ["metropolitan area network", "campus area network", "storage area network"],
        "topic": "1.4 Networks of Many Sizes",
        "explanation": "Small home networks connect a few computers to each other and to the Internet."
    },
    {
        "q": "A network setup that enables computers within a home or remote office to connect back to a corporate network is called a ____.",
        "a": "Small Office/Home Office (SOHO)",
        "distractors": ["storage area network", "global area network", "personal intranet"],
        "topic": "1.4 Networks of Many Sizes",
        "explanation": "A SOHO network enables a computer within a home or remote office to connect to a corporate network."
    },
    {
        "q": "A network infrastructure that connects many locations with hundreds or thousands of interconnected computers is a ____.",
        "a": "medium to large network",
        "distractors": ["small home network", "peer workgroup", "personal area network"],
        "topic": "1.4 Networks of Many Sizes",
        "explanation": "Medium to large networks have many locations with hundreds or thousands of computers."
    },
    {
        "q": "A network connecting hundreds of millions of computers worldwide, such as the internet, is classified as a ____.",
        "a": "worldwide network",
        "distractors": ["campus network", "metropolitan network", "local workgroup"],
        "topic": "1.4 Networks of Many Sizes",
        "explanation": "Worldwide networks connect hundreds of millions of computers globally."
    },
    {
        "q": "A network infrastructure that spans a small geographical area and provides high-speed bandwidth to internal end devices is a ____.",
        "a": "Local Area Network (LAN)",
        "distractors": ["Wide Area Network (WAN)", "Storage Area Network (SAN)", "Personal Area Network (PAN)"],
        "topic": "1.4 LANs and WANs",
        "explanation": "A LAN is a network infrastructure that spans a small geographical area."
    },
    {
        "q": "A network infrastructure that spans a wide geographical area to interconnect distant LANs is called a ____.",
        "a": "Wide Area Network (WAN)",
        "distractors": ["Local Area Network (LAN)", "Controller Area Network (CAN)", "Near Field Network (NFN)"],
        "topic": "1.4 LANs and WANs",
        "explanation": "A WAN spans a wide geographical area and interconnects LANs across cities or regions."
    },
    {
        "q": "Unlike a WAN which is managed by service providers, a LAN is typically administered by a single organization or ____.",
        "a": "individual",
        "distractors": ["government consortium", "public utility commission", "international committee"],
        "topic": "1.4 LANs and WANs",
        "explanation": "LANs are administered by a single organization or individual."
    },
    {
        "q": "Between LANs and WANs, the network type that typically provides slower speed transmission links between sites is a ____.",
        "a": "WAN",
        "distractors": ["LAN", "SOHO", "SAN"],
        "topic": "1.4 LANs and WANs",
        "explanation": "WANs typically provide slower speed links between interconnected LANs."
    },
    {
        "q": "The worldwide collection of interconnected LANs and WANs that is not owned by any single individual or group is called the ____.",
        "a": "Internet",
        "distractors": ["Intranet", "Extranet", "Ethernet"],
        "topic": "1.4 The Internet",
        "explanation": "The Internet is a worldwide collection of interconnected LANs and WANs."
    },
    {
        "q": "WAN infrastructures that interconnect LANs across the globe may use copper wires, wireless transmissions, and ____.",
        "a": "fiber-optic cables",
        "distractors": ["token-ring circuits", "serial patch bays", "loopback interfaces"],
        "topic": "1.4 The Internet",
        "explanation": "WANs may use copper wires, fiber optic cables, and wireless transmissions."
    },
    {
        "q": "The open international standards organization responsible for developing and maintaining Internet protocols and standards is the ____.",
        "a": "IETF",
        "distractors": ["IEEE", "ITU-T", "ANSI"],
        "topic": "1.4 The Internet",
        "explanation": "The Internet Engineering Task Force (IETF) develops and promotes Internet standards."
    },
    {
        "q": "The non-profit organization responsible for coordinating the allocation of global IP addresses and DNS domain names is ____.",
        "a": "ICANN",
        "distractors": ["IETF", "W3C", "ISO"],
        "topic": "1.4 The Internet",
        "explanation": "ICANN coordinates IP address allocation and Domain Name System management."
    },
    {
        "q": "The technical body responsible for the overall architectural oversight of Internet standards and protocols is the ____.",
        "a": "IAB",
        "distractors": ["FCC", "NIST", "EIA"],
        "topic": "1.4 The Internet",
        "explanation": "The Internet Architecture Board (IAB) helps maintain structure and architecture on the Internet."
    },
    {
        "q": "A private collection of LANs and WANs internal to an organization accessible exclusively to authorized members is an ____.",
        "a": "intranet",
        "distractors": ["extranet", "internet", "darknet"],
        "topic": "1.4 Intranets and Extranets",
        "explanation": "An intranet is a private internal network meant only for organization members."
    },
    {
        "q": "A network that provides secure, authenticated access to an organization's network for external partners, vendors, or customers is an ____.",
        "a": "extranet",
        "distractors": ["intranet", "internet", "ethernet"],
        "topic": "1.4 Intranets and Extranets",
        "explanation": "An extranet provides secure access to external individuals who work for different organizations."
    },

    # 1.5 Internet Connections
    {
        "q": "An always-on, high-bandwidth Internet connection offered over television coaxial cabling by cable TV providers is called ____.",
        "a": "cable",
        "distractors": ["DSL", "dial-up", "ISDN"],
        "topic": "1.5 Internet Connections",
        "explanation": "Cable provides high bandwidth, always-on internet offered by cable television providers."
    },
    {
        "q": "A high-bandwidth, always-on Internet connection that runs over traditional copper telephone lines is called ____.",
        "a": "DSL",
        "distractors": ["satellite", "cable", "cellular"],
        "topic": "1.5 Internet Connections",
        "explanation": "DSL (Digital Subscriber Line) is a high-bandwidth, always-on connection over telephone lines."
    },
    {
        "q": "An Internet access technology that uses a mobile phone cellular network to connect end devices to the Internet is called ____.",
        "a": "cellular",
        "distractors": ["powerline", "fiber-optic", "dial-up"],
        "topic": "1.5 Internet Connections",
        "explanation": "Cellular internet connects devices using a cell phone network."
    },
    {
        "q": "An Internet access technology that provides a major benefit to rural areas lacking terrestrial Internet Service Providers is ____.",
        "a": "satellite",
        "distractors": ["Metro Ethernet", "SDSL", "Leased Line"],
        "topic": "1.5 Internet Connections",
        "explanation": "Satellite internet provides a major benefit to rural areas without standard ISPs."
    },
    {
        "q": "An inexpensive, low-bandwidth Internet connection that operates over a standard analog telephone line using a modem is ____.",
        "a": "dial-up telephone",
        "distractors": ["DSL", "broadband cable", "wireless broadband"],
        "topic": "1.5 Internet Connections",
        "explanation": "Dial-up telephone is an inexpensive, low-bandwidth option using a modem and phone line."
    },
    {
        "q": "A reserved, private circuit within a service provider's network connecting distant corporate offices for voice and data is a ____.",
        "a": "dedicated leased line",
        "distractors": ["dial-up circuit", "consumer DSL line", "public hotspot"],
        "topic": "1.5 Businesses Internet Connections",
        "explanation": "Dedicated leased lines are reserved circuits connecting distant offices with private networking."
    },
    {
        "q": "A business-class connection technology that extends familiar LAN access technology directly into the wide area network is Metro Ethernet or ____.",
        "a": "Ethernet WAN",
        "distractors": ["Frame Relay", "ATM switch", "Token Ring WAN"],
        "topic": "1.5 Businesses Internet Connections",
        "explanation": "Ethernet WAN (Metro Ethernet) extends LAN access technology into the WAN."
    },
    {
        "q": "A business-grade DSL variant that provides identical bandwidth for both upload and download speeds is called ____.",
        "a": "SDSL",
        "distractors": ["ADSL", "VDSL", "Dial-up"],
        "topic": "1.5 Businesses Internet Connections",
        "explanation": "Symmetric Digital Subscriber Line (SDSL) provides symmetric bandwidth for businesses."
    },
    {
        "q": "Before converged networks, an organization was separately cabled for data, video, and ____.",
        "a": "telephone",
        "distractors": ["electrical power", "security intercom", "HVAC controls"],
        "topic": "1.5 The Converging Network",
        "explanation": "Traditionally, organizations had separate cabling for telephone, video, and data networks."
    },
    {
        "q": "A network infrastructure that delivers data, voice, and video over a single unified link using the same set of rules and standards is a ____.",
        "a": "converged network",
        "distractors": ["segmented network", "dual-ring network", "circuit-switched network"],
        "topic": "1.5 The Converging Network",
        "explanation": "Converged networks carry multiple services (data, voice, video) on one link using unified standards."
    },

    # 1.6 Reliable Networks
    {
        "q": "The technologies and structural design that support the underlying infrastructure moving data across a network are called network ____.",
        "a": "architecture",
        "distractors": ["bandwidth", "telemetry", "firmware"],
        "topic": "1.6 Reliable Networks",
        "explanation": "Network Architecture refers to the technologies that support the infrastructure moving data."
    },
    {
        "q": "The four basic characteristics that underlying network architectures must address are scalability, QoS, security, and ____.",
        "a": "fault tolerance",
        "distractors": ["low cost", "high latency", "manual routing"],
        "topic": "1.6 Reliable Networks",
        "explanation": "The 4 basic requirements of a reliable network are Fault Tolerance, Scalability, QoS, and Security."
    },
    {
        "q": "A network design characteristic that limits the impact of a failure by limiting the number of affected devices is called ____.",
        "a": "fault tolerance",
        "distractors": ["traffic shaping", "network scaling", "bandwidth capping"],
        "topic": "1.6 Fault Tolerance",
        "explanation": "A fault tolerant network limits the impact of a failure by requiring multiple redundant paths."
    },
    {
        "q": "To achieve fault tolerance and redundancy, reliable modern networks implement a ____.",
        "a": "packet-switched network",
        "distractors": ["circuit-switched network", "token-passing bus", "centralized hub"],
        "topic": "1.6 Fault Tolerance",
        "explanation": "Reliable networks provide redundancy by implementing a packet-switched network."
    },
    {
        "q": "In a packet-switched network, traffic is split into packets where each packet can theoretically take a different path to the ____.",
        "a": "destination",
        "distractors": ["default gateway only", "central mainframe", "local broadcast domain"],
        "topic": "1.6 Fault Tolerance",
        "explanation": "Packet switching splits traffic into packets that can each take a different path to the destination."
    },
    {
        "q": "A network architecture that establishes dedicated physical circuits between endpoints before communication begins is a ____.",
        "a": "circuit-switched network",
        "distractors": ["packet-switched network", "converged network", "peer-to-peer network"],
        "topic": "1.6 Fault Tolerance",
        "explanation": "Circuit-switched networks establish dedicated circuits, unlike packet-switched networks."
    },
    {
        "q": "The characteristic of a network that allows it to expand quickly and easily to support new users and applications without degrading existing performance is ____.",
        "a": "scalability",
        "distractors": ["fault tolerance", "confidentiality", "latency"],
        "topic": "1.6 Scalability",
        "explanation": "A scalable network can expand quickly and easily to support new users without impacting performance."
    },
    {
        "q": "Network designers follow accepted international standards and protocols primarily to ensure networks are ____.",
        "a": "scalable",
        "distractors": ["proprietary", "circuit-switched", "centralized"],
        "topic": "1.6 Scalability",
        "explanation": "Standards and protocols enable network equipment from diverse vendors to scale seamlessly."
    },
    {
        "q": "The primary network mechanism used to prioritize time-sensitive traffic like voice and live video to ensure reliable delivery is ____.",
        "a": "Quality of Service (QoS)",
        "distractors": ["Network Address Translation (NAT)", "Dynamic Host Configuration (DHCP)", "Access Control Lists (ACL)"],
        "topic": "1.6 Quality of Service",
        "explanation": "Quality of Service (QoS) is the primary mechanism used to ensure reliable delivery of content."
    },
    {
        "q": "Watching an online video that suffers from constant pauses and stutter occurs when demand exceeds bandwidth and ____ is not configured.",
        "a": "QoS",
        "distractors": ["DNS", "DHCP", "SSH"],
        "topic": "1.6 Quality of Service",
        "explanation": "Breaks and pauses in streaming video happen when demand exceeds bandwidth and QoS isn't configured."
    },
    {
        "q": "Network security that addresses the physical protection of routers, switches, and cabling from unauthorized access is ____.",
        "a": "network infrastructure security",
        "distractors": ["information security", "cloud virtualization", "application logic"],
        "topic": "1.6 Network Security",
        "explanation": "Network infrastructure security involves physical security and preventing unauthorized device access."
    },
    {
        "q": "Network security that focuses on protecting the actual data transmitted over the network is called ____.",
        "a": "information security",
        "distractors": ["infrastructure security", "hardware diagnostics", "cable management"],
        "topic": "1.6 Network Security",
        "explanation": "Information security protects the information or data transmitted over the network."
    },
    {
        "q": "The goal of network security that ensures only intended recipients can read data is ____.",
        "a": "confidentiality",
        "distractors": ["integrity", "availability", "scalability"],
        "topic": "1.6 Network Security",
        "explanation": "Confidentiality ensures that only intended recipients can read the data."
    },
    {
        "q": "The goal of network security that provides assurance that data has not been altered or tampered with during transmission is ____.",
        "a": "integrity",
        "distractors": ["confidentiality", "availability", "non-repudiation"],
        "topic": "1.6 Network Security",
        "explanation": "Integrity provides assurance that the data has not been altered during transmission."
    },
    {
        "q": "The goal of network security that ensures authorized users have timely and dependable access to data and services is ____.",
        "a": "availability",
        "distractors": ["confidentiality", "integrity", "privacy"],
        "topic": "1.6 Network Security",
        "explanation": "Availability provides assurance of timely and reliable access to data for authorized users."
    },

    # 1.7 Network Trends
    {
        "q": "The growing trend that allows end users to use personal tools and devices to access corporate information is known as ____.",
        "a": "Bring Your Own Device (BYOD)",
        "distractors": ["Internet of Things (IoT)", "Network Virtualization", "Data Center Bridging"],
        "topic": "1.7 Bring Your Own Device",
        "explanation": "Bring Your Own Device (BYOD) allows users to use their personal devices for work and communication."
    },
    {
        "q": "BYOD is summarized by the philosophy of allowing any device, with any ownership, to be used ____.",
        "a": "anywhere",
        "distractors": ["anonymously", "in secret", "without an IP address"],
        "topic": "1.7 Bring Your Own Device",
        "explanation": "BYOD means 'any device, with any ownership, used anywhere'."
    },
    {
        "q": "Working with others over the network on joint projects and sharing interactive content in real time is called online ____.",
        "a": "collaboration",
        "distractors": ["virtualization", "segmentation", "benchmarking"],
        "topic": "1.7 Online Collaboration",
        "explanation": "Online collaboration allows users to work with others over the network on joint projects."
    },
    {
        "q": "A multifunctional Cisco collaboration application that allows users to send messages, post images, and share video is Cisco ____.",
        "a": "Webex Teams",
        "distractors": ["Packet Tracer", "Network Assistant", "SecureCRT"],
        "topic": "1.7 Online Collaboration",
        "explanation": "Cisco Webex Teams is a multifunctional collaboration tool for messaging, images, videos, and links."
    },
    {
        "q": "An integrated enterprise video conferencing solution that delivers an immersive face-to-face meeting experience across distances is Cisco ____.",
        "a": "TelePresence",
        "distractors": ["AnyConnect", "Firepower", "Prime"],
        "topic": "1.7 Video Communication",
        "explanation": "Cisco TelePresence powers interactive video collaboration where everyone can meet from anywhere."
    },
    {
        "q": "The computing model that allows users and businesses to store personal files or backup data on remote servers over the Internet is ____.",
        "a": "cloud computing",
        "distractors": ["powerline networking", "terminal emulation", "edge slicing"],
        "topic": "1.7 Cloud Computing",
        "explanation": "Cloud computing allows us to store personal files or backup data on servers over the Internet."
    },
    {
        "q": "Cloud computing is physically made possible through massive computing and storage facilities known as ____.",
        "a": "data centers",
        "distractors": ["telecommunication closets", "repeater stations", "wiring racks"],
        "topic": "1.7 Cloud Computing",
        "explanation": "Cloud computing is made possible by data centers from which companies lease server/storage services."
    },
    {
        "q": "A cloud deployment model available to the general public through a pay-per-use model or for free is a ____.",
        "a": "public cloud",
        "distractors": ["private cloud", "hybrid cloud", "custom cloud"],
        "topic": "1.7 Cloud Computing",
        "explanation": "Public clouds are available to the general public through a pay-per-use model or for free."
    },
    {
        "q": "A cloud computing infrastructure intended exclusively for a specific organization or entity such as the government is a ____.",
        "a": "private cloud",
        "distractors": ["public cloud", "hybrid cloud", "custom cloud"],
        "topic": "1.7 Cloud Computing",
        "explanation": "Private clouds are intended for a specific organization or entity such as the government."
    },
    {
        "q": "A cloud architecture made up of two or more cloud types where each part remains distinctive but connected using the same architecture is a ____.",
        "a": "hybrid cloud",
        "distractors": ["custom cloud", "unified cloud", "partitioned cloud"],
        "topic": "1.7 Cloud Computing",
        "explanation": "Hybrid clouds are composed of two or more cloud types (e.g., part custom and part public)."
    },
    {
        "q": "A cloud environment built specifically to meet the specialized needs and regulations of a specific industry like healthcare is a ____.",
        "a": "custom cloud",
        "distractors": ["general cloud", "public cloud", "baseline cloud"],
        "topic": "1.7 Cloud Computing",
        "explanation": "Custom clouds are built to meet the needs of a specific industry, such as healthcare or media."
    },
    {
        "q": "The growing trend that integrates networking and intelligence into everyday appliances like ovens and thermostats is ____.",
        "a": "smart home technology",
        "distractors": ["industrial automation", "dark fiber", "edge computing"],
        "topic": "1.7 Technology Trends in the Home",
        "explanation": "Smart home technology integrates technology into everyday appliances to interconnect them."
    },
    {
        "q": "A networking solution that allows devices to connect to a LAN using existing electrical wiring and standard wall outlets is ____.",
        "a": "powerline networking",
        "distractors": ["satellite broadband", "cellular tethering", "optical switching"],
        "topic": "1.7 Powerline Networking",
        "explanation": "Powerline networking allows devices to connect to a LAN using existing electrical outlets."
    },
    {
        "q": "Powerline networking is especially useful in homes when wireless access points cannot reach all devices and data cables are not a viable ____.",
        "a": "option",
        "distractors": ["protocol", "threat", "topology"],
        "topic": "1.7 Powerline Networking",
        "explanation": "Powerline networking connects devices where network cables or wireless are not viable options."
    },
    {
        "q": "An Internet Service Provider commonly found in rural environments that connects subscribers to designated wireless access points is a ____.",
        "a": "Wireless Internet Service Provider (WISP)",
        "distractors": ["Dial-up Carrier", "Cable Operator", "Satellite Fleet"],
        "topic": "1.7 Wireless Broadband",
        "explanation": "A WISP connects subscribers to designated access points or hotspots in rural environments."
    },
    {
        "q": "Wireless broadband solutions for homes and small businesses use the same cellular technology found in a ____.",
        "a": "smartphone",
        "distractors": ["rotary phone", "walkie-talkie", "cable modem"],
        "topic": "1.7 Wireless Broadband",
        "explanation": "Wireless broadband uses the same cellular technology used by a smartphone."
    },

    # 1.8 Network Security & 1.9 IT Professional
    {
        "q": "Malicious code and attacks such as viruses, worms, and Trojan horses originating outside the network are classified as ____.",
        "a": "external threats",
        "distractors": ["internal threats", "system vulnerabilities", "physical hazards"],
        "topic": "1.8 Security Threats",
        "explanation": "External threats originate outside an organization and include viruses, worms, and Trojans."
    },
    {
        "q": "A network attack that exploits an undocumented software vulnerability on the very day it is discovered before a patch exists is a ____.",
        "a": "zero-day attack",
        "distractors": ["dictionary attack", "brute-force attack", "replay attack"],
        "topic": "1.8 Security Threats",
        "explanation": "Zero-day attacks exploit software vulnerabilities on day one of discovery before patches exist."
    },
    {
        "q": "A network attack designed to overwhelm network servers or devices with traffic to prevent legitimate users from accessing services is a ____.",
        "a": "denial of service attack",
        "distractors": ["phishing attack", "spyware scan", "privilege breach"],
        "topic": "1.8 Security Threats",
        "explanation": "Denial of Service (DoS) attacks disable services by swamping them with excessive traffic."
    },
    {
        "q": "Security risks originating from within an organization, such as lost or stolen devices and accidental employee mistakes, are ____.",
        "a": "internal threats",
        "distractors": ["external threats", "botnet assaults", "zero-day exploits"],
        "topic": "1.8 Security Threats",
        "explanation": "Internal threats include lost/stolen devices, accidental misuse by employees, and malicious staff."
    },
    {
        "q": "A foundational security solution on home and small office networks used to inspect and block unauthorized incoming traffic is a ____.",
        "a": "firewall",
        "distractors": ["repeater", "bridge", "unmanaged hub"],
        "topic": "1.8 Security Solutions",
        "explanation": "Firewall filtering blocks unauthorized access to the network."
    },
    {
        "q": "On enterprise networks, a series of sequential permit or deny statements used on routers to filter traffic based on IP addresses is an ____.",
        "a": "Access Control List (ACL)",
        "distractors": ["Address Resolution Table", "CAM table", "Dynamic Routing Table"],
        "topic": "1.8 Security Solutions",
        "explanation": "Access Control Lists (ACL) filter network traffic based on IP addresses and services."
    },
    {
        "q": "A dedicated security appliance that actively monitors network traffic to detect and block fast-spreading threats like zero-day attacks is an ____.",
        "a": "Intrusion Prevention System (IPS)",
        "distractors": ["Uninterruptible Power Supply", "Network Interface Card", "Media Converter"],
        "topic": "1.8 Security Solutions",
        "explanation": "An Intrusion Prevention System (IPS) actively identifies and mitigates fast-spreading attacks."
    },
    {
        "q": "A technology that provides encrypted, secure communication channels over an untrusted public network for teleworkers is a ____.",
        "a": "Virtual Private Network (VPN)",
        "distractors": ["Local Area Network", "Wide Area Network", "Dynamic Host Protocol"],
        "topic": "1.8 Security Solutions",
        "explanation": "Virtual Private Networks (VPN) provide secure remote access for employees over the Internet."
    },
    {
        "q": "The foundational industry certification that demonstrates knowledge of IP foundation, security, automation, and wireless is the ____.",
        "a": "CCNA",
        "distractors": ["CompTIA A+", "CISSP", "PMP"],
        "topic": "1.9 The IT Professional",
        "explanation": "The Cisco Certified Network Associate (CCNA) certification validates foundational networking knowledge."
    },
    {
        "q": "Cisco's certification track at associate, specialist, and professional levels designed to validate software development and programmability skills is ____.",
        "a": "DevNet",
        "distractors": ["CyberOps", "CCIE", "Routing & Switching"],
        "topic": "1.9 The IT Professional",
        "explanation": "DevNet certifications validate software development and network programmability skills."
    },
    {
        "q": "On www.netacad.com, Networking Academy students and alumni can search for jobs with Cisco and partner employers using the ____.",
        "a": "Talent Bridge Matching Engine",
        "distractors": ["Cisco Job Matcher", "Career Netlink", "Cisco Talent Scout"],
        "topic": "1.9 The IT Professional",
        "explanation": "The Talent Bridge Matching Engine connects students and alumni with job opportunities."
    }
]
