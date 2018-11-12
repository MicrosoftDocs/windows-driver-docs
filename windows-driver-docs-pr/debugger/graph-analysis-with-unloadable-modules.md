---
title: Graph Analysis with Unloadable Modules
description: Graph Analysis with Unloadable Modules
ms.assetid: 12441fa1-3d19-4485-815c-546367f31567
keywords: ["kernel streaming debugging, unloadable modules"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Graph Analysis with Unloadable Modules


This section describes a scenario that may affect you if you are working with unloadable modules such as KMixer.

After loading, the extension module initializes at the first command usage. At initialization, the extension module checks whether every module is loaded and has correct symbols. If any individual module is unloaded or has incorrect symbols loaded, the extension disables the library extension which handles identification, dumping, etc. for that module. In this case, you need to manually re-enable the disabled module.

The above situation may occur if you load the extension at boot time. Specifically, you may encounter this scenario if you load Ks.dll and then issue a [**.reboot**](-reboot--reboot-target-computer-.md) command. Or, it could happen if you break into the debugger during boot and load Ks.dll at that point.

In the following example, we are capturing two streams (sndrec32) from a Telex USB microphone. Breaking on **splitter!FilterProcess** and running [**!ks.graph**](-ks-graph.md) on splitter's filter yields:

```dbgcmd
kd> !graph ffa0c6d4 7
Attempting a graph build on ffa0c6d4...  Please be patient...
Graph With Starting Point ffa0c6d4:
"usbaudio" Filter ffaaa768, Child Factories 2
    Output Factory 0:
        Pin ffb1caf0 (File 811deeb8, -> "splitter" ffa8b008) Irps(q/p) = 7, 1
"splitter" Filter ffa0c660, Child Factories 2
    Output Factory 0:
        Pin 81250008 (File ffb10028) Irps(q/p) = 3, 0
        Pin 811df9c0 (File ffaaf2f0) Irps(q/p) = 3, 0
    Input Factory 1:
        Pin ffa8b008 (File ffb26d68, <- "usbaudio" ffb1caf0) Irps(q/p) = 1, 7
```

In this example, KMixer has been loaded and connected to splitter, but Kmixer does not appear in the graph. There are IRPs queued to splitter's output pin, yet the **!ks.graph** command is unable to backtrace and discover KMixer. Issue a [**!ks.libexts details**](-ks-libexts.md) command to investigate further:

```dbgcmd
kd> !libexts details
## LibExt Details:
--------------------------------------------------
LibExt "portcls!" :
    Status :  ACTIVE
    This is the port class library extension to the KS DLL.  It supports
    dumping wave cyclic, wave pci, irp streams, and several other upper
    level structures.
    Commands Exported: pciaudio
    Help : pchelp
    Hooks : dump dumpqueue dumpcircuit conv(file) conv(device) graph
LibExt "STREAM!" :
    Status :  ACTIVE
    This is the stream class library extension to the KS DLL.  It supports
    dumping device extensions, filters, streams, and SRBs.
    Hooks : dump enumdevobj graph
LibExt "kmixer!" :
    Status :  INACTIVE
    This is the KMIXER extension to the KS DLL.  It supports
    virtually nothing at this point!
    Hooks : dump graph
```

According to the above output, the KMixer section of the extension is currently disabled (Status : INACTIVE). Since the extension module was first used in a context in which KMixer was not loaded, Ks.dll has disabled the KMixer section of the extension to prevent time-consuming references to an unloaded module.

To enable KMixer explicitly, you can use [**!ks.libexts**](-ks-libexts.md) with the **enable** parameter, as follows:

```dbgcmd
kd> !libexts enable kmixer
LibExt "kmixer" has been enabled.

kd> !graph ffa0c6d4 7
Attempting a graph build on ffa0c6d4...  Please be patient...
Graph With Starting Point ffa0c6d4:
"usbaudio" Filter ffaaa768, Child Factories 2
    Output Factory 0:
        Pin ffb1caf0 (File 811deeb8, -> "splitter" ffa8b008) Irps(q/p) = 7, 1
"splitter" Filter ffa0c660, Child Factories 2
    Output Factory 0:
        Pin 81250008 (File ffb10028, -> "kmixer" 8123c000) Irps(q/p) = 3, 0
        Pin 811df9c0 (File ffaaf2f0, -> "kmixer" 81236000) Irps(q/p) = 3, 0
    Input Factory 1:
        Pin ffa8b008 (File ffb26d68, <- "usbaudio" ffb1caf0) Irps(q/p) = 1, 7
"kmixer" Filter ffa65b70, Child Factories 4
    Input Factory 2:
        Pin 81236000 (File ffaaf7d0, <- "splitter" 811df9c0) Irps(q/p) = 0, 0
    Output Factory 3:
        Pin 81252d00 (File 811df1d8) Irps(q/p) = 10, 0
"kmixer" Filter ffb03808, Child Factories 4
    Input Factory 2:
        Pin 8123c000 (File ffb10130, <- "splitter" 81250008) Irps(q/p) = 0, 0
    Output Factory 3:
        Pin ffa1e9c0 (File 81253468) Irps(q/p) = 10, 0
```

KMixer now appears as expected in the capture graph.

 

 





