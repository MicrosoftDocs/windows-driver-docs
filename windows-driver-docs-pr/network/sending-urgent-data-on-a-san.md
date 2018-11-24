---
title: Sending Urgent Data on a SAN
description: Sending Urgent Data on a SAN
ms.assetid: 9ff9719a-dd42-4ce7-8c07-370afa17fd7b
keywords:
- urgent data WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending Urgent Data on a SAN





If an application sends urgent data on a SAN, the Windows Sockets switch transfers that data as described in the following sequence:

1.  For requests to send urgent data, the switch receives a **WSPSend** call in which the MSG\_OOB flag is set.

2.  The switch copies the urgent data to the payload portion of a control message buffer.

3.  The switch calls the appropriate SAN service provider's [**WSPSend**](https://msdn.microsoft.com/library/windows/hardware/ff566316) function to transmit the urgent data contained in the control message to the remote peer connection for a SAN socket. The SAN NIC in turn transmits the urgent data.

4.  The switch at the remote peer receives the transmitted data into receive buffers that it posted with the [**WSPRecv**](https://msdn.microsoft.com/library/windows/hardware/ff566309) function.

5.  The switch at the remote peer copies the received data from the receive buffers to private storage.

6.  The switch at the remote peer calls **WSPRecv** to repost the receive buffers.

7.  The switch at the remote peer delivers the data to an application in accordance with standard Windows Sockets procedures.

 

 





