---
title: Differences Between the HD Audio DDI Versions
description: Differences Between the HD Audio DDI Versions
ms.assetid: e24071d3-9021-40c0-907a-91ada8a1306b
keywords:
- HD Audio, DDI version differences
- High Definition Audio (HD Audio), DDI version differences
- HDAUDIO_BUS_INTERFACE structure
- HDAUDIO_BUS_INTERFACE_BDL structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences Between the HD Audio DDI Versions


The HD Audio DDI is available in three slightly different versions that are defined as follows:

-   A baseline version of the HD Audio DDI, which is defined by the [**HDAUDIO\_BUS\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536413) structure. Most function drivers for audio and modem codecs require only the capabilities that this DDI version provides. This version is available through the HD Audio bus drivers that are provided with Windows XP and Windows Vista.

-   An enhanced version of the HD Audio DDI that is defined by the [**HDAUDIO\_BUS\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff536418) structure. This version of the DDI provides the additional capability that is required to support DMA-driven event notification with flexibility. It is available in Windows Vista and later versions of Windows.

-   A modified version of the HD Audio DDI that is defined by the [**HDAUDIO\_BUS\_INTERFACE\_BDL**](https://msdn.microsoft.com/library/windows/hardware/ff536416) structure. This version accommodates the requirements of a relatively few audio and modem drivers that must have additional control over the setup of buffer descriptor lists (BDLs) for DMA operations. This version of the DDI is available for Windows XP and later versions of Windows. However, use either the HDAUDIO\_BUS\_INTERFACE or the HDAUDIO\_BUS\_INTERFACE\_V2 DDI version instead. .

In all three structures, the names and types of the first five members match those of the five members of the [**INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff547825) structure. For information about the values of these members, see [Obtaining an HDAUDIO\_BUS\_INTERFACE DDI Object](obtaining-an-hdaudio-bus-interface-ddi-object.md), [Obtaining an HDAUDIO\_BUS\_INTERFACE\_V2 DDI Object](obtaining-an-hdaudio-bus-interface-v2-ddi-object.md) or [Obtaining an HDAUDIO\_BUS\_INTERFACE\_BDL DDI Object](obtaining-an-hdaudio-bus-interface-bdl-ddi-object.md).

The routines in the three versions of the HD Audio DDI perform the following tasks:

-   Transfer commands to codecs and retrieve the responses to those commands.

-   Allocate and set up DMA engines to transfer the data in render and capture streams.

-   Change the stream state of one or more DMA engines to running, paused, stopped, or reset.

-   Reserve link bandwidth for render and capture streams.

-   Provide direct access to the wall clock register and link position registers.

-   Notify clients of unsolicited responses from codecs.

-   Register kernel events so that they can receive DMA progress notifications.

The HDAUDIO\_BUS\_INTERFACE and HDAUDIO\_BUS\_INTERFACE\_BDL versions of the DDI have the following differences:

-   The HDAUDIO\_BUS\_INTERFACE structure defines two routines, [**AllocateDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536179) and [**FreeDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536391), that are not present in HDAUDIO\_BUS\_INTERFACE\_BDL.

-   The HDAUDIO\_BUS\_INTERFACE\_BDL structure defines three routines, [**SetupDmaEngineWithBdl**](https://msdn.microsoft.com/library/windows/hardware/ff537894), [**AllocateContiguousDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536178), and [**FreeContiguousDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536390), that are not present in HDAUDIO\_BUS\_INTERFACE.

When a client calls the **AllocateDmaBuffer** routine in the first DDI version, the HD Audio bus driver:

-   Allocates a DMA buffer and BDL for a DMA engine to use.

-   Initializes the BDL.

-   Sets up the DMA engine to use the buffer and BDL.

In contrast, the **AllocateContiguousDmaBuffer** routine in the second DDI version allocates storage for a DMA buffer and BDL, but relies on the caller to initialize the BDL. The **SetupDmaEngineWithBdl** routine sets up the DMA engine to use the buffer and the caller-initialized BDL.

The BDL contains the list of physical memory blocks in the DMA engine's scatter/gather queue. By calling **SetupDmaEngineWithBdl** to set up the BDL, the client can specify the points in the data stream at which the DMA engine generates interrupts. The client does this by setting the interrupt-on-completion (IOC) bit in selected BDL entries. With this capability, the client can precisely control the timing of the IOC interrupts that occur during the processing of the audio stream. Audio modem drivers also use the second DDI version to get accurate system clock information.

For more information, see the *Intel High Definition Audio Specification*.

However, nearly all clients will use the HDAUDIO\_BUS\_INTERFACE version of the DDI. Only a few clients that require precise control over the timing of interrupts will use the HDAUDIO\_BUS\_INTERFACE\_BDL version.

 

 




