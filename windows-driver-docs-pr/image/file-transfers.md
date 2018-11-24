---
title: File Transfers
description: File Transfers
ms.assetid: 1c776dc5-982a-4652-bc03-f334fda30055
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File Transfers





**Note**   File transfers are for operating systems prior to Windows Vista.

 

A *file data transfer* is a transfer of image data from the WIA minidriver into a file that the WIA service created. The WIA application that initiates the data transfer indicates to the WIA service that it is ready to perform a file transfer.

The WIA service then creates a file and instructs the WIA minidriver to transfer data into the file. The WIA minidriver contacts the device by requesting the data to be transferred. The minidriver requires its own memory, so the lower-level bus driver stack is able to place the acquired data into the buffer. When the WIA minidriver receives the data in its buffer, it uses the [**wiasWriteBufToFile**](https://msdn.microsoft.com/library/windows/hardware/ff549473) WIA service library function, passing in its memory buffer. The WIA service library then writes the contents of the WIA minidriver's memory buffer into the file that the WIA service created, as the following diagram shows.

![diagram illustrating a wia driver file data transfer](images/wia-imagedatafile.png)

Use the **wiasWriteBufToFile** service library function for most file transfers. Use the [**wiasWritePageBufToFile**](https://msdn.microsoft.com/library/windows/hardware/ff549484) service library function only for drivers that require the WIA service to write multipage TIFF files. Drivers that use their own TIFF headers when they write multipage TIFF files should use **wiasWriteBufToFile**.

 

 




