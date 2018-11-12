---
title: NDIS Extensions (Ndiskd.dll)
description: NDIS Extensions (Ndiskd.dll)
ms.assetid: bf4a7cc2-0116-4d6d-8a6f-2e9dc77d3631
keywords: ["NDIS extensions (ndiskd.dll)", "ndiskd.dll (NDIS extensions)", "extensions, NDIS"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# NDIS Extensions (Ndiskd.dll)


## <span id="ddk_ndis_extensions_ndiskd_dll__dbg"></span><span id="DDK_NDIS_EXTENSIONS_NDISKD_DLL__DBG"></span>


This section describes commands available in !ndiskd, a debugger extension that is useful for debugging NDIS (Network Device Interface Specification) drivers. These commands enable network driver developers to see a bigger picture of the Windows networking stack and how their drivers interact with it. With !ndiskd, you can see the state of all network adapters ([**!ndiskd.netadapter**](-ndiskd-netadapter.md)), a visual diagram of the computer's network stack ([**!ndiskd.netreport**](-ndiskd-netreport.md)), a log of traffic on the network adapters([**!ndiskd.nbllog**](-ndiskd-nbllog.md)), or a list of all pending OID requests ([**!ndiskd.oid**](-ndiskd-oid.md)).

The commands can be found in Ndiskd.dll. To load the symbols, enter **.reload /f ndis.sys** in the debugger command window. To confirm the symbols loaded successfully, use the [**!lmi ndis**](-lmi.md) extension and look for the phrase "Symbols loaded successfully" toward the bottom. Your output should look similar to the following example:

```dbgcmd
3: kd> !lmi ndis
Loaded Module Info: [ndis] 
         Module: ndis
   Base Address: fffff80e2e150000
     Image Name: ndis.sys
   Machine Type: 34404 (X64)
     Time Stamp: 57f4c58d Wed Oct  5 02:19:09 2016
           Size: 128000
       CheckSum: 1213f7
Characteristics: 22  
Debug Data Dirs: Type  Size     VA  Pointer
             CODEVIEW    21, 7b1b8,   79fb8 RSDS - GUID: {06A2E58C-996D-4419-81A0-BB293BD63BCA}
               Age: 1, Pdb: ndis.pdb
                   ??   880, 7b1dc,   79fdc [Data not mapped]
     Image Type: MEMORY   - Image read successfully from loaded memory.
    Symbol Type: PDB      - Symbols loaded successfully from image header.
                 c:\Debuggers\sym\ndis.pdb\06A2E58C996D441981A0BB293BD63BCA1\ndis.pdb
       Compiler: Linker - front end [0.0 bld 0] - back end [14.0 bld 23917]
    Load Report: private symbols & lines, source indexed 
                 c:\Debuggers\sym\ndis.pdb\06A2E58C996D441981A0BB293BD63BCA1\ndis.pdb
```

## <span id="_ndiskd_Hyperlinks"></span><span id="_ndiskd_hyperlinks"></span><span id="_NDISKD_HYPERLINKS"></span>!ndiskd Hyperlinks


Many of the extension commands in !ndiskd present you with hyperlinks in the results they display in the debugger window. The text for these hyperlinks has been left in the samples provided to illustrate the exact format of what you will see when you run the command on your debugee machine. Some of the examples also refer explicitly to clicking on these links so you can understand typical usage flows, though the examples also provide the alternate command line forms of each command.

## <span id="Common_Parameters"></span><span id="common_parameters"></span><span id="COMMON_PARAMETERS"></span>Common Parameters


All !ndiskd commands support the following generic parameters.

<span id="_______-verbose______"></span><span id="_______-VERBOSE______"></span> *-verbose*   
Shows additional details.

<span id="_______-terse______"></span><span id="_______-TERSE______"></span> *-terse*   
Suppresses some boilerplate output.

<span id="_______-static______"></span><span id="_______-STATIC______"></span> *-static*   
Suppresses some interactive output.

<span id="_______-dml_0_1______"></span><span id="_______-DML_0_1______"></span> *-dml 0|1*   
Controls whether DML (debugger markup language) output is enabled.

<span id="_______-unicode_0_1______"></span><span id="_______-UNICODE_0_1______"></span> *-unicode 0|1*   
Controls whether Unicode character output is allowed.

<span id="_______-indent_N______"></span><span id="_______-indent_n______"></span><span id="_______-INDENT_N______"></span> *-indent N*   
Uses *N* spaces per level of indent.

<span id="_______-force______"></span><span id="_______-FORCE______"></span> *-force*   
Overrides some safety checks on remote data sanity.

<span id="_______-tracedata______"></span><span id="_______-TRACEDATA______"></span> *-tracedata*   
Shows verbose trace messages to debug !ndiskd itself.

## <span id="Net_Adapter__NDIS_Driver__and_General_Commands"></span><span id="net_adapter__ndis_driver__and_general_commands"></span><span id="NET_ADAPTER__NDIS_DRIVER__AND_GENERAL_COMMANDS"></span>Net Adapter, NDIS Driver, and General Commands


The following commands display information about the machine's network adapters, network drivers, and general commands associated with the network stack (such as rcvqueues, opens, filters, OIDs, and RW locks).

-   [**!ndiskd.netadapter**](-ndiskd-netadapter.md)
-   [**!ndiskd.minidriver**](-ndiskd-minidriver.md)
-   [**!ndiskd.rcvqueue**](-ndiskd-rcvqueue.md)
-   [**!ndiskd.protocol**](-ndiskd-protocol.md)
-   [**!ndiskd.mopen**](-ndiskd-mopen.md)
-   [**!ndiskd.filter**](-ndiskd-filter.md)
-   [**!ndiskd.filterdriver**](-ndiskd-filterdriver.md)
-   [**!ndiskd.oid**](-ndiskd-oid.md)
-   [**!ndiskd.ndisrwlock**](-ndiskd-ndisrwlock.md)
-   [**!ndiskd.netreport**](-ndiskd-netreport.md)

## <span id="NET_BUFFER_LIST_and_NET_BUFFER_Commands"></span><span id="net_buffer_list_and_net_buffer_commands"></span><span id="NET_BUFFER_LIST_AND_NET_BUFFER_COMMANDS"></span>NET\_BUFFER\_LIST and NET\_BUFFER Commands


The following commands display information relating to [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure) and [**NET\_BUFFER**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-structure) structures.

-   [**!ndiskd.nbl**](-ndiskd-nbl.md)
-   [**!ndiskd.nb**](-ndiskd-nb.md)
-   [**!ndiskd.nblpool**](-ndiskd-nblpool.md)
-   [**!ndiskd.nbpool**](-ndiskd-nbpool.md)
-   [**!ndiskd.pendingnbls**](-ndiskd-pendingnbls.md)
-   [**!ndiskd.nbllog**](-ndiskd-nbllog.md)

## <span id="NetAdapterCx_Commands"></span><span id="netadaptercx_commands"></span><span id="NETADAPTERCX_COMMANDS"></span>NetAdapterCx Commands


The following commands display information relating to the Network Adapter WDF Class Extension (NetAdapterCx)\[LINK TBD\] and its associated structures, NET\_RING\_BUFFER \[LINK TBD\] and NET\_PACKET \[LINK TBD\].

-   [**!ndiskd.cxadapter**](-ndiskd-cxadapter.md)
-   [**!ndiskd.netqueue**](-ndiskd-netqueue.md)
-   [**!ndiskd.netrb**](-ndiskd-netrb.md)
-   [**!ndiskd.netpacket**](-ndiskd-netpacket.md)
-   [**!ndiskd.netpacketfragment**](-ndiskd-netpacketfragment.md)

## <span id="Network_Interface_Commands"></span><span id="network_interface_commands"></span><span id="NETWORK_INTERFACE_COMMANDS"></span>Network Interface Commands


The following commands display information relating to network interfaces.

-   [**!ndiskd.interfaces**](-ndiskd-interfaces.md)
-   [**!ndiskd.ifprovider**](-ndiskd-ifprovider.md)

## <span id="NDIS_PACKET_Commands"></span><span id="ndis_packet_commands"></span><span id="NDIS_PACKET_COMMANDS"></span>NDIS\_PACKET Commands


The following commands display information about [NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures. These extensions are for legacy NDIS 5.x drivers. The NDIS\_PACKET structure and its associated architecture have been deprecated.

-   [**!ndiskd.pkt**](-ndiskd-pkt.md)
-   [**!ndiskd.pktpools**](-ndiskd-pktpools.md)
-   [**!ndiskd.findpacket**](-ndiskd-findpacket.md)

## <span id="CoNDIS_Commands"></span><span id="condis_commands"></span><span id="CONDIS_COMMANDS"></span>CoNDIS Commands


The following commands display information about [Connection-Oriented NDIS](https://msdn.microsoft.com/windows/hardware/drivers/network/connection-oriented-ndis) connections.

-   [**!ndiskd.vc**](-ndiskd-vc.md)
-   [**!ndiskd.af**](-ndiskd-af.md)

## <span id="NDIS_Debugging_Commands"></span><span id="ndis_debugging_commands"></span><span id="NDIS_DEBUGGING_COMMANDS"></span>NDIS Debugging Commands


The following commands display information relating to NDIS refcounts, event logs, stack traces, and debug traces.

-   [**!ndiskd.ndisref**](-ndiskd-ndisref.md)
-   [**!ndiskd.ndisevent**](-ndiskd-ndisevent.md)
-   [**!ndiskd.ndisstack**](-ndiskd-ndisstack.md)
-   [**!ndiskd.dbglevel**](-ndiskd-dbglevel.md)
-   [**!ndiskd.dbgsystems**](-ndiskd-dbgsystems.md)

## <span id="WDI_Commands"></span><span id="wdi_commands"></span><span id="WDI_COMMANDS"></span>WDI Commands


The following commands display information about [WDI Miniport Drivers](https://msdn.microsoft.com/windows/hardware/drivers/network/wdi-miniport-driver-design-guide).

-   [**!ndiskd.wdiadapter**](-ndiskd-wdiadapter.md)
-   [**!ndiskd.wdiminidriver**](-ndiskd-wdiminidriver.md)
-   [**!ndiskd.nwadapter**](-ndiskd-nwadapter.md)

## <span id="NDIS_and__ndiskd_Information_Commands"></span><span id="ndis_and__ndiskd_information_commands"></span><span id="NDIS_AND__NDISKD_INFORMATION_COMMANDS"></span>NDIS and !ndiskd Information Commands


The following commands display information about NDIS.sys and ndiskd.dll.

-   [**!ndiskd.ndis**](-ndiskd-ndis.md)
-   [**!ndiskd.ndiskdversion**](-ndiskd-ndiskdversion.md)

## <span id="Miscellaneous_Commands"></span><span id="miscellaneous_commands"></span><span id="MISCELLANEOUS_COMMANDS"></span>Miscellaneous Commands


-   [**!ndiskd.ifstacktable**](-ndiskd-ifstacktable.md)
-   [**!ndiskd.compartments**](-ndiskd-compartments.md)
-   [**!ndiskd.ndisslot**](-ndiskd-ndisslot.md)

## <span id="Related_Topics"></span><span id="related_topics"></span><span id="RELATED_TOPICS"></span>Related Topics


For more information about designing NDIS drivers for Windows Vista and later, see the [Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index).

For more information about reference for NDIS drivers for Windows Vista and later, see [Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081).

For a demonstration of using the !ndiskd debugger commands to debug the network stack, see [Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311).

 

 






