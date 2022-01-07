---
title: Reading Restart Records from a CLFS Stream
description: Reading Restart Records from a CLFS Stream
keywords: ["Common Log File System WDK kernel , restart records", "CLFS WDK kernel , restart records", "restart records WDK CLFS", "reading restart records"]
ms.date: 06/16/2017
---

# Reading Restart Records from a CLFS Stream





To read all of the restart records in a Common Log File System (CLFS) stream (in reverse order), use the following procedure.

1.  Call [**ClfsReadRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadrestartarea) to obtain a read context and the restart record that was most recently written to the stream.

2.  Pass the read context you obtained in step 1 to [**ClfsReadPreviousRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadpreviousrestartarea) repeatedly to obtain the remaining restart records in the log.

**Note**  When you call [**ClfsWriteRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfswriterestartarea) to write a restart record to a stream, CLFS automatically sets the previous LSN of that record to the LSN of the previous restart record in the stream. Those previous LSNs form the chain that is followed by repeated calls to **ClfsReadPreviousRestartArea**.

 

 

