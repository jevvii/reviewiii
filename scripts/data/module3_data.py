# module3_data.py
# Comprehensive question items for Module 3: Protocols and Models (Cisco CCNA 1: ITN v7.0)

MODULE_3_ITEMS = [
    # -------------------------------------------------------------------------
    # 3.1 The Rules - Communications Fundamentals & Protocols
    # -------------------------------------------------------------------------
    {
        "q": "In any network communication, the sending device where a message originates is known as the ____.",
        "a": "source (sender)",
        "distractors": ["destination (receiver)", "channel (media)", "default gateway"],
        "topic": "3.1 The Rules - Fundamentals",
        "explanation": "All communication begins with a source (sender) that creates and sends the message."
    },
    {
        "q": "In network communications, the receiving device that accepts and decodes the message is called the ____.",
        "a": "destination (receiver)",
        "distractors": ["source (sender)", "channel (media)", "repeater"],
        "topic": "3.1 The Rules - Fundamentals",
        "explanation": "The destination (receiver) is the target device that receives and interprets the transmitted message."
    },
    {
        "q": "The physical medium or path providing the transmission pathway over which messages travel from sender to receiver is called the ____.",
        "a": "channel (media)",
        "distractors": ["protocol suite", "frame check sequence", "data link layer"],
        "topic": "3.1 The Rules - Fundamentals",
        "explanation": "The channel consists of the media (copper wires, optical fibers, or wireless radio frequencies) that provides the physical path for communication."
    },
    {
        "q": "The three fundamental elements present in every network communication are the source, destination, and ____.",
        "a": "channel (media)",
        "distractors": ["default gateway", "firewall", "router"],
        "topic": "3.1 The Rules - Fundamentals",
        "explanation": "Every communication requires three elements: a source (sender), a destination (receiver), and a channel (media)."
    },
    {
        "q": "The established rules and agreements that govern how devices communicate across a network are known as ____.",
        "a": "protocols",
        "distractors": ["topologies", "bandwidths", "latencies"],
        "topic": "3.1 The Rules - Protocols",
        "explanation": "Protocols are the formal sets of rules and standards that govern data communications."
    },
    {
        "q": "A human or computer conversation cannot proceed effectively without an identified sender, receiver, common language, speed/timing, and confirmation or ____ requirements.",
        "a": "acknowledgment",
        "distractors": ["encryption", "segmentation", "multiplexing"],
        "topic": "3.1 The Rules - Rule Establishment",
        "explanation": "Effective communication requires rule establishment including acknowledgment (confirmation that messages were received)."
    },
    {
        "q": "The process of converting human-readable data or information into another acceptable electronic or optical form for transmission across a medium is called ____.",
        "a": "encoding",
        "distractors": ["decoding", "de-encapsulation", "routing"],
        "topic": "3.1 The Rules - Message Encoding",
        "explanation": "Encoding converts data into an acceptable form for transmission over the physical channel."
    },
    {
        "q": "The process where a receiving device reverses the encoding process to convert signals back into readable information is called ____.",
        "a": "decoding",
        "distractors": ["segmentation", "encapsulation", "multiplexing"],
        "topic": "3.1 The Rules - Message Encoding",
        "explanation": "Decoding reverses encoding at the destination host to reconstruct the original message."
    },
    {
        "q": "When messages are sent across a network medium, they are broken down and transmitted as patterns of electrical impulses, sound waves, or light representing ____.",
        "a": "bits",
        "distractors": ["packets", "segments", "frames"],
        "topic": "3.1 The Rules - Message Size",
        "explanation": "Messages on the network are ultimately converted into bits and encoded into physical signals (light, electricity, or radio waves)."
    },
    {
        "q": "The timing mechanism that manages the rate of data transmission to prevent a fast sender from overwhelming a slow receiver is called ____.",
        "a": "flow control",
        "distractors": ["access method", "response timeout", "carrier sensing"],
        "topic": "3.1 The Rules - Message Timing",
        "explanation": "Flow control manages transmission rate, defining how much information can be sent and at what speed."
    },
    {
        "q": "The timing rule that dictates how long a transmitting device waits for an acknowledgment or reply before assuming the message was lost is called the ____.",
        "a": "response timeout",
        "distractors": ["propagation delay", "flow control", "jitter buffer"],
        "topic": "3.1 The Rules - Message Timing",
        "explanation": "Response timeout manages how long a sending device waits for a reply before retransmitting or aborting."
    },
    {
        "q": "The rule that determines when a device is permitted to send a message across shared media to prevent transmission conflicts is the ____.",
        "a": "access method",
        "distractors": ["flow control", "modulation method", "session timeout"],
        "topic": "3.1 The Rules - Message Timing",
        "explanation": "The access method determines when a device can transmit onto shared network media."
    },
    {
        "q": "A condition where two or more devices simultaneously transmit data signals across a shared medium causing signals to corrupt each other is called a ____.",
        "a": "collision",
        "distractors": ["broadcast storm", "deadlock", "crossover"],
        "topic": "3.1 The Rules - Message Timing",
        "explanation": "A collision occurs when multiple devices transmit traffic at the exact same moment on a shared channel, corrupting both messages."
    },
    {
        "q": "The message delivery method where information is transmitted from a single source host directly to a single destination host is called ____.",
        "a": "unicast",
        "distractors": ["broadcast", "multicast", "anycast"],
        "topic": "3.1 The Rules - Delivery Options",
        "explanation": "Unicast refers to one-to-one communication between a single sender and single receiver."
    },
    {
        "q": "The message delivery option where a message is sent from one source to a selected group of destination hosts that subscribed to receive it is called ____.",
        "a": "multicast",
        "distractors": ["unicast", "broadcast", "anycast"],
        "topic": "3.1 The Rules - Delivery Options",
        "explanation": "Multicast is one-to-many communication, delivering to a specific subset of hosts."
    },
    {
        "q": "The message delivery method in IPv4 where a packet is sent from a single sender to all hosts on the local network segment is called ____.",
        "a": "broadcast",
        "distractors": ["unicast", "multicast", "anycast"],
        "topic": "3.1 The Rules - Delivery Options",
        "explanation": "Broadcast is one-to-all communication on a local network segment."
    },
    {
        "q": "Unlike IPv4, the IPv6 protocol does not implement broadcast messaging; instead, it uses multicast and a special one-to-nearest delivery option called ____.",
        "a": "anycast",
        "distractors": ["simulcast", "unicast only", "geocast"],
        "topic": "3.1 The Rules - Delivery Options",
        "explanation": "IPv6 eliminated traditional broadcast in favor of multicast and anycast (one-to-nearest)."
    },
    {
        "q": "In Cisco network documentation and topology diagrams, client computers, servers, and intermediate devices are frequently represented using a generic circular symbol called the ____.",
        "a": "node icon",
        "distractors": ["bus bar", "bridge glyph", "cloud token"],
        "topic": "3.1 The Rules - Node Icon",
        "explanation": "Network diagrams frequently use a circular node icon to represent any network-connected device."
    },

    # -------------------------------------------------------------------------
    # 3.2 Protocols - Types & Functions
    # -------------------------------------------------------------------------
    {
        "q": "Network protocols can be implemented in device hardware, device software, or ____.",
        "a": "both hardware and software",
        "distractors": ["firmware only", "virtual machines only", "cloud storage only"],
        "topic": "3.2 Protocols - Overview",
        "explanation": "Protocols can be implemented in software (like OS drivers and applications), hardware (like NIC chipsets), or both."
    },
    {
        "q": "The protocol category responsible for enabling two or more devices to exchange data packets over one or more interconnected networks is ____.",
        "a": "network communications",
        "distractors": ["network security", "routing", "service discovery"],
        "topic": "3.2 Protocols - Protocol Types",
        "explanation": "Network communications protocols (e.g., IP, TCP, HTTP) enable devices to communicate across networks."
    },
    {
        "q": "The protocol category that provides data encryption, user authentication, and data integrity verification is ____.",
        "a": "network security",
        "distractors": ["service discovery", "routing", "multiplexing"],
        "topic": "3.2 Protocols - Protocol Types",
        "explanation": "Network security protocols (like SSH, TLS/SSL, IPsec) provide confidentiality, integrity, and authentication."
    },
    {
        "q": "The protocol type that enables routers to exchange network path information, compare metrics, and select the best path to destination networks is ____.",
        "a": "routing",
        "distractors": ["service discovery", "error detection", "flow control"],
        "topic": "3.2 Protocols - Protocol Types",
        "explanation": "Routing protocols (e.g., OSPF, EIGRP, BGP) discover routes and calculate optimal forwarding paths."
    },
    {
        "q": "The protocol category used for the automatic detection of devices, network services, and resources on a local network without manual configuration is ____.",
        "a": "service discovery",
        "distractors": ["routing", "network security", "congestion control"],
        "topic": "3.2 Protocols - Protocol Types",
        "explanation": "Service discovery protocols (e.g., DNS-SD, DHCP, mDNS) automatically identify available network services."
    },
    {
        "q": "The network protocol function that uniquely identifies the sending device and receiving device on a network is ____.",
        "a": "addressing",
        "distractors": ["sequencing", "reliability", "flow control"],
        "topic": "3.2 Protocols - Functions",
        "explanation": "Addressing provides source and destination identification (such as MAC addresses and IP addresses)."
    },
    {
        "q": "The protocol function that guarantees the delivery of data and provides retransmission if packets are lost during transit is ____.",
        "a": "reliability",
        "distractors": ["best-effort delivery", "service discovery", "carrier sense"],
        "topic": "3.2 Protocols - Functions",
        "explanation": "Reliability services (such as TCP acknowledgments and retransmissions) guarantee that sent data arrives intact."
    },
    {
        "q": "The protocol function that numbers or uniquely labels each transmitted data piece so that they can be reassembled in the correct order is called ____.",
        "a": "sequencing",
        "distractors": ["multiplexing", "error detection", "addressing"],
        "topic": "3.2 Protocols - Functions",
        "explanation": "Sequencing assigns sequence numbers to segments so the receiver can reassemble them in the original sequence."
    },
    {
        "q": "The protocol function that determines whether transmitted bits became corrupted or altered during transmission across the physical media is ____.",
        "a": "error detection",
        "distractors": ["error simulation", "access control", "flow control"],
        "topic": "3.2 Protocols - Functions",
        "explanation": "Error detection (such as checksums or Frame Check Sequence / CRC) detects damaged bits during transmission."
    },
    {
        "q": "The protocol function that manages direct process-to-process communication between software applications running on different hosts is the ____.",
        "a": "application interface",
        "distractors": ["routing table", "flow control", "channel arbitration"],
        "topic": "3.2 Protocols - Functions",
        "explanation": "The application interface function enables inter-process communication between host applications (e.g., port numbers and APIs)."
    },
    {
        "q": "The application layer protocol that governs how web browsers (clients) request web pages from web servers is ____.",
        "a": "HTTP (Hypertext Transfer Protocol)",
        "distractors": ["FTP", "SMTP", "SNMP"],
        "topic": "3.2 Protocols - Interaction",
        "explanation": "HTTP defines the format and interactions between web clients and web servers."
    },
    {
        "q": "In web traffic, the transport layer protocol that manages individual conversations, divides data into segments, and guarantees reliable delivery is ____.",
        "a": "TCP (Transmission Control Protocol)",
        "distractors": ["UDP", "IP", "ICMP"],
        "topic": "3.2 Protocols - Interaction",
        "explanation": "TCP provides connection-oriented, reliable transmission, flow control, and segment sequencing."
    },
    {
        "q": "The internet layer protocol that encapsulates segments into packets and delivers them globally across intermediate routers from source to destination is ____.",
        "a": "IP (Internet Protocol)",
        "distractors": ["Ethernet", "TCP", "ARP"],
        "topic": "3.2 Protocols - Interaction",
        "explanation": "IP handles logical addressing and delivers packets across interconnected networks."
    },
    {
        "q": "The network access layer protocol standard that delivers data frames from one network interface card (NIC) to another NIC on the same local Ethernet LAN is ____.",
        "a": "Ethernet",
        "distractors": ["IP", "TCP", "HTTP"],
        "topic": "3.2 Protocols - Interaction",
        "explanation": "Ethernet governs local physical transmission and frame delivery between NICs on a LAN."
    },

    # -------------------------------------------------------------------------
    # 3.3 Protocol Suites - Evolution & TCP/IP
    # -------------------------------------------------------------------------
    {
        "q": "A group of inter-related protocols that work cooperatively across different layers to perform network communication functions is called a ____.",
        "a": "protocol suite",
        "distractors": ["routing table", "domain namespace", "broadcast domain"],
        "topic": "3.3 Protocol Suites - Overview",
        "explanation": "A protocol suite is an organized collection of complementary protocols that solve communication problems together."
    },
    {
        "q": "In a layered protocol suite, the lower layers are primarily responsible for moving data across the physical media and providing services to the ____.",
        "a": "upper layers",
        "distractors": ["BIOS only", "firmware chip only", "adjacent routers only"],
        "topic": "3.3 Protocol Suites - Layer Architecture",
        "explanation": "Lower layers handle physical transmission and data delivery, offering services to the upper layers."
    },
    {
        "q": "The universal, open-standard protocol suite that powers the modern internet and enterprise networks is the ____ suite.",
        "a": "TCP/IP",
        "distractors": ["AppleTalk", "Novell NetWare", "Decnet"],
        "topic": "3.3 Protocol Suites - Evolution",
        "explanation": "The TCP/IP suite is the dominant protocol suite used across the global Internet and local networks."
    },
    {
        "q": "The TCP/IP protocol suite is maintained, updated, and standardized by the ____.",
        "a": "IETF (Internet Engineering Task Force)",
        "distractors": ["IEEE", "ITU-T", "EIA"],
        "topic": "3.3 Protocol Suites - Evolution",
        "explanation": "The IETF manages and standardizes the protocols of the TCP/IP suite through RFC documents."
    },
    {
        "q": "The historical proprietary protocol suite developed and released by Apple Inc. for Macintosh local networking in the 1980s was ____.",
        "a": "AppleTalk",
        "distractors": ["Novell NetWare", "DECnet", "OSI Suite"],
        "topic": "3.3 Protocol Suites - Evolution",
        "explanation": "AppleTalk was Apple's proprietary suite before adopting the standard TCP/IP model."
    },
    {
        "q": "The historical proprietary protocol suite that included IPX/SPX and was widely used in early enterprise local area networks was ____.",
        "a": "Novell NetWare",
        "distractors": ["AppleTalk", "SNA", "Ethernet II"],
        "topic": "3.3 Protocol Suites - Evolution",
        "explanation": "Novell NetWare used IPX/SPX as its proprietary protocol stack before modern TCP/IP dominance."
    },
    {
        "q": "A protocol specification that is published without proprietary vendor restrictions, freely available to the public, and usable by anyone is called an ____.",
        "a": "open standard",
        "distractors": ["closed proprietary system", "commercial license", "trade secret"],
        "topic": "3.3 Protocol Suites - Open Standards",
        "explanation": "Open standards ensure vendor neutrality and allow any company or developer to implement the technology."
    },
    {
        "q": "A protocol suite that is endorsed by the networking industry and ratified by an official standards organization to guarantee multi-vendor interoperability is termed ____.",
        "a": "standards-based",
        "distractors": ["vendor-locked", "ad-hoc", "proprietary"],
        "topic": "3.3 Protocol Suites - Standards",
        "explanation": "Standards-based protocols have been approved by standards organizations to ensure interoperability between diverse manufacturers."
    },
    {
        "q": "The two most prevalent Network Access layer local area network (LAN) technologies in the TCP/IP model are Ethernet and ____.",
        "a": "WLAN (Wireless LAN)",
        "distractors": ["Token Ring", "FDDI", "ATM"],
        "topic": "3.3 Protocol Suites - TCP/IP Examples",
        "explanation": "Ethernet (wired) and WLAN (wireless, IEEE 802.11) are the two primary network access LAN technologies."
    },

    # -------------------------------------------------------------------------
    # 3.4 Standards Organizations
    # -------------------------------------------------------------------------
    {
        "q": "Standards organizations that develop network protocols must be non-profit, open to the public, and ____.",
        "a": "vendor-neutral",
        "distractors": ["vendor-specific", "government-operated only", "privately commercial"],
        "topic": "3.4 Standards Organizations - Open Standards",
        "explanation": "Standards organizations remain vendor-neutral so no single corporation controls fundamental network standards."
    },
    {
        "q": "Open networking standards encourage three major market benefits: interoperability, innovation, and ____.",
        "a": "competition",
        "distractors": ["monopoly", "vendor lock-in", "planned obsolescence"],
        "topic": "3.4 Standards Organizations - Benefits",
        "explanation": "Open standards encourage interoperability, market competition, and rapid innovation."
    },
    {
        "q": "The non-profit organization dedicated to ensuring the open development, evolution, and ethical use of the Internet worldwide is the ____.",
        "a": "ISOC (Internet Society)",
        "distractors": ["IAB", "ICANN", "IANA"],
        "topic": "3.4 Standards Organizations - Internet Bodies",
        "explanation": "The Internet Society (ISOC) promotes open development and global evolution of the Internet."
    },
    {
        "q": "The committee responsible for overall architectural oversight, technical management, and appeal procedures for Internet standards is the ____.",
        "a": "IAB (Internet Architecture Board)",
        "distractors": ["IETF", "IRTF", "IEEE"],
        "topic": "3.4 Standards Organizations - Internet Bodies",
        "explanation": "The IAB manages internet architecture, advises ISOC, and supervises IETF standards processes."
    },
    {
        "q": "The working group organization that develops, tests, and maintains internet standards and TCP/IP protocols via RFC documents is the ____.",
        "a": "IETF (Internet Engineering Task Force)",
        "distractors": ["IRTF", "ICANN", "ITU-T"],
        "topic": "3.4 Standards Organizations - Internet Bodies",
        "explanation": "The IETF produces RFC (Request for Comments) documents that define Internet and TCP/IP standards."
    },
    {
        "q": "The organization that focuses on long-term theoretical research topics related to the Internet, TCP/IP, and future protocol architectures is the ____.",
        "a": "IRTF (Internet Research Task Force)",
        "distractors": ["IETF", "ISOC", "EIA"],
        "topic": "3.4 Standards Organizations - Internet Bodies",
        "explanation": "The IRTF focuses on long-term research groups, whereas the IETF focuses on short-to-medium term engineering."
    },
    {
        "q": "The international non-profit entity that coordinates global IP address space allocation, top-level domain (TLD) names, and protocol identifiers is ____.",
        "a": "ICANN (Internet Corporation for Assigned Names and Numbers)",
        "distractors": ["IANA", "IETF", "ISOC"],
        "topic": "3.4 Standards Organizations - IP Coordination",
        "explanation": "ICANN coordinates IP address allocation, DNS domain management, and protocol parameters globally."
    },
    {
        "q": "The operational department overseen by ICANN that directly manages the global allocation of IPv4/IPv6 address blocks, AS numbers, and root DNS zones is ____.",
        "a": "IANA (Internet Assigned Numbers Authority)",
        "distractors": ["IETF", "IAB", "IRTF"],
        "topic": "3.4 Standards Organizations - IP Coordination",
        "explanation": "IANA performs the operational responsibility for assigning IP addresses, protocol numbers, and port assignments."
    },
    {
        "q": "The global professional organization that created the 802 LAN/MAN standards, including 802.3 Ethernet and 802.11 Wi-Fi, is the ____.",
        "a": "IEEE (Institute of Electrical and Electronics Engineers)",
        "distractors": ["EIA", "TIA", "ITU-T"],
        "topic": "3.4 Standards Organizations - Electronics Standards",
        "explanation": "IEEE defines fundamental electrical and computer engineering standards such as 802.3 (Ethernet) and 802.11 (WLAN)."
    },
    {
        "q": "The trade organization known for standardizing electrical wiring pinouts, serial connectors, and standard 19-inch equipment racks is the ____.",
        "a": "EIA (Electronic Industries Alliance)",
        "distractors": ["IEEE", "ISOC", "ICANN"],
        "topic": "3.4 Standards Organizations - Electronics Standards",
        "explanation": "EIA developed physical standards for electrical wiring, connectors, and equipment racks."
    },
    {
        "q": "The standards body responsible for developing communication standards in radio equipment, cellular towers, VoIP terminals, and satellite communications is the ____.",
        "a": "TIA (Telecommunications Industry Association)",
        "distractors": ["IAB", "IANA", "IRTF"],
        "topic": "3.4 Standards Organizations - Electronics Standards",
        "explanation": "TIA standardizes telecommunications equipment, cabling (such as TIA/EIA-568), and radio frequencies."
    },
    {
        "q": "The specialized United Nations agency sector responsible for international standards in video compression, IPTV, and broadband communications like DSL is the ____.",
        "a": "ITU-T (Telecommunication Standardization Sector of ITU)",
        "distractors": ["IEEE", "IETF", "ICANN"],
        "topic": "3.4 Standards Organizations - Electronics Standards",
        "explanation": "ITU-T defines international telecommunications standards including video codecs (H.264), DSL, and optical transport."
    },

    # -------------------------------------------------------------------------
    # 3.5 Reference Models - OSI vs TCP/IP
    # -------------------------------------------------------------------------
    {
        "q": "One primary advantage of using a layered networking model is that changes in technology or capabilities at one layer do not affect ____.",
        "a": "other layers above and below",
        "distractors": ["the speed of light", "physical cable lengths", "the destination host IP address"],
        "topic": "3.5 Reference Models - Layered Benefits",
        "explanation": "Layer independence ensures changes or upgrades in one layer do not require redesigning adjacent layers."
    },
    {
        "q": "A layered model fosters healthy vendor competition because hardware and software from different vendors can ____.",
        "a": "interoperate (work together)",
        "distractors": ["be purchased from a single supplier", "bypass standard security policies", "avoid electrical grounding"],
        "topic": "3.5 Reference Models - Layered Benefits",
        "explanation": "Standardized layer interfaces allow products from different manufacturers to interoperate seamlessly."
    },
    {
        "q": "How many distinct architectural layers are defined in the theoretical OSI reference model?",
        "a": "7",
        "distractors": ["4", "5", "8"],
        "topic": "3.5 Reference Models - OSI Model",
        "explanation": "The OSI model consists of 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application."
    },
    {
        "q": "How many architectural layers are defined in the practical TCP/IP reference model?",
        "a": "4",
        "distractors": ["7", "5", "6"],
        "topic": "3.5 Reference Models - TCP/IP Model",
        "explanation": "The TCP/IP model consists of 4 layers: Network Access, Internet, Transport, and Application."
    },
    {
        "q": "In the OSI reference model, Layer 7 is the ____ layer.",
        "a": "Application",
        "distractors": ["Presentation", "Session", "Transport"],
        "topic": "3.5 Reference Models - OSI Model",
        "explanation": "Layer 7 of the OSI model is the Application layer, providing services directly to user network software."
    },
    {
        "q": "In the OSI model, the layer responsible for data formatting, data compression, and data encryption/decryption between applications is the ____ layer.",
        "a": "Presentation (Layer 6)",
        "distractors": ["Session (Layer 5)", "Transport (Layer 4)", "Application (Layer 7)"],
        "topic": "3.5 Reference Models - OSI Model",
        "explanation": "The Presentation layer ensures common data representation, data compression, and encryption."
    },
    {
        "q": "The OSI model layer that establishes, manages, synchronizes, and terminates communication dialogues between cooperating applications is the ____ layer.",
        "a": "Session (Layer 5)",
        "distractors": ["Presentation (Layer 6)", "Transport (Layer 4)", "Network (Layer 3)"],
        "topic": "3.5 Reference Models - OSI Model",
        "explanation": "The Session layer manages dialogues and data exchange sessions between applications."
    },
    {
        "q": "The OSI layer that segments, transfers, and reassembles data for individual communications between end hosts is the ____ layer.",
        "a": "Transport (Layer 4)",
        "distractors": ["Network (Layer 3)", "Data Link (Layer 2)", "Session (Layer 5)"],
        "topic": "3.5 Reference Models - OSI Model",
        "explanation": "Layer 4 (Transport) defines services to segment, transfer, and reassemble conversation data."
    },
    {
        "q": "The OSI layer responsible for logical addressing, path determination, and forwarding packets across intermediate networks is the ____ layer.",
        "a": "Network (Layer 3)",
        "distractors": ["Data Link (Layer 2)", "Transport (Layer 4)", "Physical (Layer 1)"],
        "topic": "3.5 Reference Models - OSI Model",
        "explanation": "Layer 3 (Network) handles logical addressing (IP) and exchanges individual pieces of data across networks."
    },
    {
        "q": "The OSI layer responsible for exchanging data frames across a common physical medium and managing physical MAC addressing is the ____ layer.",
        "a": "Data Link (Layer 2)",
        "distractors": ["Physical (Layer 1)", "Network (Layer 3)", "Session (Layer 5)"],
        "topic": "3.5 Reference Models - OSI Model",
        "explanation": "Layer 2 (Data Link) describes methods for exchanging data frames over common physical media."
    },
    {
        "q": "The OSI model layer responsible for the physical connectors, cabling specifications, and transmitting raw bit signals across transmission media is the ____ layer.",
        "a": "Physical (Layer 1)",
        "distractors": ["Data Link (Layer 2)", "Network (Layer 3)", "Transport (Layer 4)"],
        "topic": "3.5 Reference Models - OSI Model",
        "explanation": "Layer 1 (Physical) specifies electrical, mechanical, and optical means to transmit raw bit streams."
    },
    {
        "q": "In the TCP/IP model, the single top layer that combines the functions of the OSI Application, Presentation, and Session layers is the ____ layer.",
        "a": "Application",
        "distractors": ["Transport", "Internet", "Network Access"],
        "topic": "3.5 Reference Models - TCP/IP Model",
        "explanation": "The TCP/IP Application layer represents data to the user and handles encoding, presentation, and dialog control."
    },
    {
        "q": "The TCP/IP layer that corresponds directly to OSI Layer 3 and determines the best path through interconnected networks is the ____ layer.",
        "a": "Internet",
        "distractors": ["Transport", "Network Access", "Application"],
        "topic": "3.5 Reference Models - TCP/IP Model",
        "explanation": "The TCP/IP Internet layer maps to OSI Layer 3 (Network) and routes packets using logical IP addressing."
    },
    {
        "q": "The TCP/IP layer that controls the physical hardware devices and media and corresponds to OSI Layers 1 and 2 is the ____ layer.",
        "a": "Network Access",
        "distractors": ["Internet", "Transport", "Physical Only"],
        "topic": "3.5 Reference Models - TCP/IP Model",
        "explanation": "The Network Access layer in the TCP/IP model encompasses both the Data Link and Physical layers of the OSI model."
    },

    # -------------------------------------------------------------------------
    # 3.6 Data Encapsulation - Segmentation, PDUs, & Stacks
    # -------------------------------------------------------------------------
    {
        "q": "The networking process of dividing a large stream of application data into smaller, manageable chunks before transmission is known as ____.",
        "a": "segmenting (segmentation)",
        "distractors": ["multiplexing", "encapsulation", "routing"],
        "topic": "3.6 Data Encapsulation - Segmenting",
        "explanation": "Segmenting breaks large messages into smaller units so they can travel across the network efficiently."
    },
    {
        "q": "The technique of taking multiple streams of segmented data from different conversations and interleaving them together over a single network channel is called ____.",
        "a": "multiplexing",
        "distractors": ["broadcasting", "de-encapsulation", "modulation"],
        "topic": "3.6 Data Encapsulation - Multiplexing",
        "explanation": "Multiplexing interleaves multiple communication streams across shared transmission channels."
    },
    {
        "q": "A major benefit of segmenting data messages is that if a piece of data fails to reach its destination, only the lost ____ needs to be retransmitted.",
        "a": "segment",
        "distractors": ["entire file", "entire database", "operating system"],
        "topic": "3.6 Data Encapsulation - Benefits",
        "explanation": "Segmentation increases efficiency because only failed segments must be retransmitted rather than the entire message."
    },
    {
        "q": "The formal term used to describe the generic package of data and protocol control information created at each layer of a networking model is a ____.",
        "a": "PDU (Protocol Data Unit)",
        "distractors": ["MTU (Maximum Transmission Unit)", "SYN packet", "MAC table entry"],
        "topic": "3.6 Data Encapsulation - PDUs",
        "explanation": "A Protocol Data Unit (PDU) is the specific form that data takes at any given layer of the protocol stack."
    },
    {
        "q": "In the TCP/IP protocol suite, what is the specific name of the PDU at the Transport layer?",
        "a": "Segment",
        "distractors": ["Packet", "Frame", "Bits"],
        "topic": "3.6 Data Encapsulation - PDUs",
        "explanation": "At the Transport layer, the PDU is called a Segment (or Datagram for UDP)."
    },
    {
        "q": "In the TCP/IP protocol suite, what is the specific name of the PDU at the Internet (Network) layer?",
        "a": "Packet",
        "distractors": ["Segment", "Frame", "Bits"],
        "topic": "3.6 Data Encapsulation - PDUs",
        "explanation": "At the Network/Internet layer, the PDU encapsulated with IP addressing is called a Packet."
    },
    {
        "q": "In the TCP/IP protocol suite, what is the specific name of the PDU at the Data Link layer?",
        "a": "Frame",
        "distractors": ["Packet", "Segment", "Bits"],
        "topic": "3.6 Data Encapsulation - PDUs",
        "explanation": "At the Data Link layer, data encapsulated with header and trailer information is called a Frame."
    },
    {
        "q": "At the Physical layer, what is the name of the PDU transmitted across the physical media as electrical, optical, or radio signals?",
        "a": "Bits",
        "distractors": ["Frames", "Packets", "Segments"],
        "topic": "3.6 Data Encapsulation - PDUs",
        "explanation": "At the Physical layer, the PDU consists of raw Bits transmitted over the physical medium."
    },
    {
        "q": "What is the correct top-down sequence of Protocol Data Units (PDUs) as data moves down the TCP/IP stack during encapsulation?",
        "a": "Data → Segment → Packet → Frame → Bits",
        "distractors": [
            "Bits → Frame → Packet → Segment → Data",
            "Data → Packet → Segment → Frame → Bits",
            "Frame → Packet → Segment → Data → Bits"
        ],
        "topic": "3.6 Data Encapsulation - PDU Order",
        "explanation": "Data moves top-down: Data (Application) → Segment (Transport) → Packet (Internet) → Frame (Data Link) → Bits (Physical)."
    },
    {
        "q": "The top-down process where each layer adds its own protocol control header (and trailer) to the data received from the layer above is called ____.",
        "a": "encapsulation",
        "distractors": ["de-encapsulation", "decryption", "demultiplexing"],
        "topic": "3.6 Data Encapsulation - Process",
        "explanation": "Encapsulation adds layer-specific protocol headers as data moves down from the application layer to the physical media."
    },
    {
        "q": "The bottom-up process where a receiving host strips off protocol headers at each successive layer to deliver the original data to the application is called ____.",
        "a": "de-encapsulation",
        "distractors": ["encapsulation", "fragmentation", "compression"],
        "topic": "3.6 Data Encapsulation - Process",
        "explanation": "De-encapsulation occurs at the receiving host, stripping each header as data moves up the protocol stack."
    },
    {
        "q": "In the encapsulation process, what transport layer protocol is specifically responsible for numbering and sequencing data segments?",
        "a": "TCP",
        "distractors": ["UDP", "IP", "ICMP"],
        "topic": "3.6 Data Encapsulation - Sequencing",
        "explanation": "TCP tracks and orders transmitted chunks using sequence numbers to guarantee accurate reassembly."
    },

    # -------------------------------------------------------------------------
    # 3.7 Data Access - Network & Data Link Addressing
    # -------------------------------------------------------------------------
    {
        "q": "The logical addressing information contained in the Layer 3 IP packet header is responsible for delivering the packet from its original source to its ____.",
        "a": "final destination",
        "distractors": ["next-hop router only", "local switch only", "default gateway MAC"],
        "topic": "3.7 Data Access - Layer 3 Addressing",
        "explanation": "Layer 3 IP addresses deliver the packet from the original sending host to the ultimate final destination host across all networks."
    },
    {
        "q": "The physical addressing information contained in the Layer 2 Data Link frame header is responsible for delivering data from one ____ to another on the same link.",
        "a": "NIC (Network Interface Card)",
        "distractors": ["autonomous system", "web server port", "domain name server"],
        "topic": "3.7 Data Access - Layer 2 Addressing",
        "explanation": "Layer 2 MAC addresses govern delivery from one NIC to the next NIC on the same local network segment."
    },
    {
        "q": "An IPv4 address consists of two functional sections: the host portion and the ____ portion.",
        "a": "network",
        "distractors": ["prefix only", "port", "MAC"],
        "topic": "3.7 Data Access - IP Structure",
        "explanation": "An IP address is hierarchically divided into a network portion (identifying the subnet) and a host portion (identifying the specific device)."
    },
    {
        "q": "In an IPv6 address, the left-most portion that identifies the network group is called the ____.",
        "a": "prefix",
        "distractors": ["interface ID", "host portion", "socket"],
        "topic": "3.7 Data Access - IP Structure",
        "explanation": "In IPv6, the network part of the address is called the prefix, while the host part is the Interface ID."
    },
    {
        "q": "In an IPv6 address, the right-most 64 bits that uniquely identify a specific host device on the local network are called the ____.",
        "a": "Interface ID",
        "distractors": ["Prefix", "Subnet Mask", "MAC Tag"],
        "topic": "3.7 Data Access - IP Structure",
        "explanation": "The Interface ID identifies the individual host interface within an IPv6 network prefix."
    },
    {
        "q": "When two communicating devices reside on the same local IP network, their IP addresses share the exact same ____ portion.",
        "a": "network",
        "distractors": ["host", "interface ID", "port number"],
        "topic": "3.7 Data Access - Same Network",
        "explanation": "Devices on the same network or subnet share identical network portions in their IP addresses."
    },
    {
        "q": "When sending data to a host located on the exact same Ethernet network, what address is placed in the Destination MAC field of the frame?",
        "a": "The MAC address of the destination device's NIC",
        "distractors": [
            "The MAC address of the default gateway router",
            "The broadcast MAC address FF-FF-FF-FF-FF-FF",
            "The source device's own MAC address"
        ],
        "topic": "3.7 Data Access - Same Network",
        "explanation": "When the destination host is on the same local network, the destination MAC address is that host's physical NIC MAC."
    },
    {
        "q": "Physical MAC addresses are permanently burned or embedded into the hardware of a device's ____.",
        "a": "NIC (Network Interface Card)",
        "distractors": ["hard drive", "operating system registry", "RAM cache"],
        "topic": "3.7 Data Access - MAC Addressing",
        "explanation": "MAC addresses are hardware-level addresses burned into the ROM of a network interface card (NIC)."
    },
    {
        "q": "When a host determines that the destination IP address belongs to a remote network, it forwards the packet to the local router interface known as the ____.",
        "a": "default gateway",
        "distractors": ["DNS server", "broadcast address", "loopback address"],
        "topic": "3.7 Data Access - Remote Network",
        "explanation": "The default gateway is the router interface on the local subnet that acts as the exit door to remote networks."
    },
    {
        "q": "If end devices on a local area network are not configured with an accurate default gateway IP address, their outbound network traffic will be confined strictly to the ____.",
        "a": "local LAN",
        "distractors": ["Internet", "cloud provider", "remote WAN"],
        "topic": "3.7 Data Access - Default Gateway",
        "explanation": "Without a configured default gateway, hosts can only communicate with other devices on their local LAN."
    },
    {
        "q": "When a source host (PC1) sends a packet to a remote web server across multiple routers, the destination MAC address in the first transmitted frame will be the MAC address of the ____.",
        "a": "default gateway (local router interface)",
        "distractors": [
            "remote web server NIC",
            "second router's exit interface",
            "local host's own loopback"
        ],
        "topic": "3.7 Data Access - Remote Frame Addressing",
        "explanation": "For remote destinations, the source host addresses the frame's destination MAC to its local default gateway router interface."
    },
    {
        "q": "As an IP packet travels across multiple router hops toward a remote destination, the source and destination IP addresses in the packet header remain ____.",
        "a": "unchanged",
        "distractors": ["incremented at each hop", "swapped at each hop", "replaced by MAC addresses"],
        "topic": "3.7 Data Access - Address Persistence",
        "explanation": "The original source IP and ultimate destination IP addresses do not change as the packet moves through intermediate routers."
    },
    {
        "q": "Unlike Layer 3 IP addresses which remain constant end-to-end, Layer 2 MAC addresses are stripped and replaced at every router ____.",
        "a": "hop (link)",
        "distractors": ["session restart", "DNS query", "TCP handshake"],
        "topic": "3.7 Data Access - Address Modification",
        "explanation": "At each router hop, the old Layer 2 frame is stripped off and a new frame with new source and destination MAC addresses is generated for the next link."
    },
    {
        "q": "When the final router on the path receives a packet destined for a host on its directly connected LAN, it encapsulates the packet in a frame whose destination MAC is the ____.",
        "a": "final destination host NIC",
        "distractors": ["first router's entry interface", "Internet Service Provider gateway", "switch management interface"],
        "topic": "3.7 Data Access - Final Delivery",
        "explanation": "On the final local subnet, the router frames the packet with the destination host's actual MAC address for final delivery."
    },
    {
        "q": "In network data access, which layer provides local physical addressing that changes from hop to hop?",
        "a": "Data Link Layer (Layer 2)",
        "distractors": ["Network Layer (Layer 3)", "Transport Layer (Layer 4)", "Application Layer (Layer 7)"],
        "topic": "3.7 Data Access - Summary",
        "explanation": "The Data Link layer provides local hop-to-hop physical addressing (MAC), whereas the Network layer provides global end-to-end logical addressing (IP)."
    },
    {
        "q": "In network data access, which layer provides global logical addressing that remains constant from the original source to the final destination?",
        "a": "Network Layer (Layer 3)",
        "distractors": ["Data Link Layer (Layer 2)", "Physical Layer (Layer 1)", "Session Layer (Layer 5)"],
        "topic": "3.7 Data Access - Summary",
        "explanation": "The Network layer (Layer 3) provides end-to-end logical addressing that does not change across routers."
    }
]
