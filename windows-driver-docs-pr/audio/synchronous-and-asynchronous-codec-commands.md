---
title: Synchronous and Asynchronous Codec Commands
description: Synchronous and Asynchronous Codec Commands
ms.assetid: c37cc94d-37eb-4a3e-b7ae-63fed8827d21
keywords:
- TransferCodecVerbs
- codec commands WDK audio
- HD Audio, codec commands
- High Definition Audio (HD Audio), codec commands
- synchronous codec commands WDK audio
- asynchronous codec commands WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronous and Asynchronous Codec Commands


The [**TransferCodecVerbs**](https://msdn.microsoft.com/library/windows/hardware/ff538596) routine allows function drivers to send commands to audio and modem codecs that are connected to an HD Audio controller. The codec commands can execute either synchronously or asynchronously:

-   If a call to [**TransferCodecVerbs**](https://msdn.microsoft.com/library/windows/hardware/ff538596) submits a list of commands to be processed synchronously, the routine returns only after the codec or codecs have processed all of the commands.

-   If a call to [**TransferCodecVerbs**](https://msdn.microsoft.com/library/windows/hardware/ff538596) submits a list of commands to be processed asynchronously, the routine returns as soon as the HD Audio bus driver adds the commands to its internal command queue, without waiting for the codec or codecs to process the commands. After the codecs have processed the commands, the bus driver notifies the function driver by calling a callback routine.

Depending on the nature of the codec commands that it sends, the function driver uses one or more of the following techniques to retrieve responses from a codec:

-   If the function driver must have the response from the codec before it can perform any additional processing, it uses the synchronous mode.

-   If the function driver does not need to wait for the codec commands to complete, to see the codec responses, and to know when the commands complete, then it uses the asynchronous mode, ignores the callback routine (except to free the storage for the codec commands), and discards or ignores the responses to the codec commands.

-   If the function driver must know when the codec commands complete, but does not need to see the responses, then it uses the asynchronous mode and relies on the callback routine for notification. However, it discards or ignores the responses to the codec commands. The callback routine might use a [kernel streaming (KS) event](https://msdn.microsoft.com/library/windows/hardware/ff567643) to send the notification to the main part of the driver.

-   If the function driver must know both when the codec commands complete and what the responses are, but must resume processing immediately rather than waiting for the commands to complete, then it uses the asynchronous mode and avoids reading the responses until it receives the callback routine. Either the callback routine or the main part of the driver can inspect the responses.

[*TransferCodecVerbs*](https://msdn.microsoft.com/library/windows/hardware/ff538596) returns STATUS\_SUCCESS if it succeeds in adding the list of commands to the bus driver's internal command queue. Even though the call succeeds, the responses might still be invalid. The function driver must check the status bits in the codec responses to determine whether they are valid. This rule applies to both synchronous and asynchronous mode.

The cause of an invalid response is likely to be one of the following:

-   The command did not reach the codec.

-   The codec responded, but the response was lost when a first-in, first-out (FIFO) overrun occurred in the RIRB.

The latter problem indicates that the RIRB FIFO is of insufficient size.

Each codec response contains an **IsValid** flag to indicate whether the response is valid and a **HasFifoOverrun** flag to indicate whether an RIRB FIFO overrun has occurred. If **IsValid** = 0, indicating that a response is invalid, the **HasFifoOverrun** flag helps identify the source of the failure:

-   If **HasFifoOverrun** = 0, then the codec failed to respond within the required time interval. The probable cause is that the command never reached the codec.

-   If **HasFifoOverrun** = 1, then the command probably reached the codec, but the response was lost due to a FIFO overrun.

During a call to *TransferCodecCommands*, the caller provides a pointer to an array of [**HDAUDIO\_CODEC\_TRANSFER**](https://msdn.microsoft.com/library/windows/hardware/ff536424) structures. Each structure contains a command and provides space for a response. The bus driver always writes each response into the structure that contains the command that triggered the response.

For each call to *TransferCodecCommands*, the order in which the commands are processed is determined by the order of the commands in the array. Processing the first command in the array always completes before processing the second command begins, and so on.

In addition, if a client makes an asynchronous call to *TransferCodecCommands* and then calls *TransferCodecCommands* a second time without waiting for the callback routine from the first call, the relative order in which the two groups of commands from the two calls are processed is defined by the order in which the client submitted the two groups of commands. Thus, the bus driver processes all of the commands from the first call before it begins processing the commands from the second call.

However, the relative order of commands sent by two different function driver instances is undefined. (Each instance has its own physical device object.) For example, if instance 1 calls *TransferCodecCommands* to send commands A, B, and C in the order A-B-C, and instance 2 calls *TransferCodecCommands* to send commands X, Y, and Z in the order X-Y-Z, then the bus driver might execute the commands in the order A-X-Y-B-Z-C.

When separate function driver threads share access to the same set of hardware resources, the relative order of commands from different driver threads might be important. If so, the function driver is responsible for synchronizing the sharing of the resources among the threads.

For example, the hardware interface for writing a sequence of data bytes to a codec might consist of an index register and an 8-bit data register. First, the function driver submits a codec command to load the starting index into the index register. Next, the driver submits a command to write the first byte of data to the data register. The index register increments following each successive write to the data register until the transfer is complete. However, if two driver threads fail to properly synchronize their access of the index and data registers, the relative order of the individual register access by the two threads is undefined and the probable result is data corruption or an invalid hardware configuration.

The [*TransferCodecVerbs*](https://msdn.microsoft.com/library/windows/hardware/ff538596) routine is available in both versions of the HD Audio DDI.

 

 




