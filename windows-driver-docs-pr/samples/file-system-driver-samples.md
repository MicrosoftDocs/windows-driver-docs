---
title: File system driver samples
description: The driver samples in this directory provide a starting point for writing a custom file system driver for your device.
ms.assetid: 9F2F995E-EA20-4877-B96C-5FF082CE886D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File system driver samples


The driver samples in this directory provide a starting point for writing a custom file system driver for your device.

## File systems


| Sample Name      | Solution                                                           | Description                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CDFS             | [cdfs](http://go.microsoft.com/fwlink/p/?LinkId=617642)            | The CD-ROM file system driver (cdfs) sample is a file system driver for removable media.                                                                                                                                                                                               |
| FastFAT          | [fastfat](http://go.microsoft.com/fwlink/p/?LinkId=620305)         | A file system driver based on the Windows inbox FastFAT file system used as a model for new file systems.                                                                                                                                                                              |
| AVScan           | [avscan](http://go.microsoft.com/fwlink/p/?LinkId=617644)          | This filter is a transaction-aware file scanner that examines data in files. Anti-virus might operate in this fashion.                                                                                                                                                                 |
| CancelSafe       | [cancelSafe](http://go.microsoft.com/fwlink/p/?LinkId=617645)      | A minifilter demonstrating the use of cancel-safe queues.                                                                                                                                                                                                                              |
| CDO              | [cdo](http://go.microsoft.com/fwlink/p/?LinkId=617646)             | An example of using a control device object (CDO) with a minifilter.                                                                                                                                                                                                                   |
| Change           | [change](http://go.microsoft.com/fwlink/p/?LinkId=617647)          | A transaction-aware filter that monitors file changes in real time.                                                                                                                                                                                                                    |
| Ctx              | [ctx](http://go.microsoft.com/fwlink/p/?LinkId=617648)             | Demonstrates how to attach contexts to instances, files, streams, and stream handles in your minifilter.                                                                                                                                                                               |
| Delete           | [delete](http://go.microsoft.com/fwlink/p/?LinkId=617649)          | Demonstrates how to detect deletions of files or streams.                                                                                                                                                                                                                              |
| Metadata Manager | [MetadataManager](http://go.microsoft.com/fwlink/p/?LinkId=617650) | Serves as an example of how to use files for storing metadata that corresponds to your minifilters. The implementation of this sample depicts scenarios in which modifications to the file might have to be blocked or the minifilter might be required to close the file temporarily. |
| Minispy          | [minispy](http://go.microsoft.com/fwlink/p/?LinkId=617651)         | A tool to monitor and log any I/O and transaction activity that occurs in the system.                                                                                                                                                                                                  |
| NameChanger      | [NameChanger](http://go.microsoft.com/fwlink/p/?LinkId=617652)     | Grafts a directory from one part of a volume's namespace to another part using a mapping. The minifilter maintains this illusion by acting as a name provider, injecting entries into directory enumerations and forwarding directory change notifications                             |
| NullFilter       | [nullFilter](http://go.microsoft.com/fwlink/p/?LinkId=617653)      | A minifilter that simply demonstrates registration with the filter manager.                                                                                                                                                                                                            |
| PassThrough      | [passThrough](http://go.microsoft.com/fwlink/p/?LinkId=617654)     | Demonstrates how to specify callback functions for different types of I/O requests.                                                                                                                                                                                                    |
| Scanner          | [scanner](http://go.microsoft.com/fwlink/p/?LinkId=617655)         | A file data scanner example. Typically, anti-virus filters are of this type.                                                                                                                                                                                                           |
| SimRep           | [simrep](http://go.microsoft.com/fwlink/p/?LinkId=617656)          | Demonstrates how a file system filter can simulate file-system like reparse-point behavior to redirect a file open to an alternate path.                                                                                                                                               |
| SwapBuffer       | [swapBuffers](http://go.microsoft.com/fwlink/p/?LinkId=617657)     | Demonstrates how to switch buffers between reads and writes of data. This technique is particularly useful for encryption filters.                                                                                                                                                     |

 

 

 




