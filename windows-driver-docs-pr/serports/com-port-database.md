---
title: COM Port Database
description: COM Port Database
ms.assetid: c9baf147-6e33-4ed2-b682-c141938eb0da
keywords:
- COM ports WDK serial devices
- serial devices WDK , COM ports
- COM port databases WDK serial devices
- COM port numbers WDK serial devices
- port numbers WDK serial devices
- releasing port numbers
- current port number usage WDK serial devices
- size WDK COM port databases
- resizing COM port databases
- databases WDK COM port databases
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COM Port Database





The system-supplied COM port database arbitrates the use of COM port numbers by [COM ports](configuration-of-com-ports.md) that are installed on the system. Microsoft Windows provides this component to facilitate installing COM ports and, in particular, to ensure that each port number is assigned, at most, to one port. The component consists of the database and a library containing functions that the installation software calls to access the database. All system-supplied installers for COM ports use the COM port database to obtain a COM port number. Although not a Plug and Play requirement, all vendor-supplied installers should also use the COM port database to obtain a COM port number.

The following topics describe how to use the COM port database to obtain a COM port number:

Structure of the COM Port Database

Opening and Closing the COM Port Database

Determining the Current Usage of COM Port Numbers

Obtaining and Releasing a COM Port Number

Resizing the COM Port Database

For information about routines that support the COM port database, see [COMPort Database Support Routines](https://msdn.microsoft.com/library/windows/hardware/ff546483).

To call these routines in an installer, link the installer to *msports.lib*, which is provided with the Windows Driver Kit (WDK).

### Structure of the COM Port Database

The COM port database consists of an array of elements, each of which indicates whether a COM port number is in use. The first array element corresponds to COM1, the second corresponds to COM2, and so on. However, the database does not contain any information about which device is assigned a given port number. The size of the database equals the number of port numbers that the database currently arbitrates. The minimum number of port numbers that the database arbitrates is COMDB\_MIN\_PORTS\_ARBITRATED, and the maximum number it arbitrates is COMDB\_MAX\_PORTS\_ARBITRATED. The size of the database can be increased by using the [**ComDBResizeDatabase**](https://msdn.microsoft.com/library/windows/hardware/ff546480) routine.

### Opening and Closing the COM Port Database

Before using the COM port database, a client must open the database by calling the [**ComDBOpen**](https://msdn.microsoft.com/library/windows/hardware/ff546476) routine to obtain a handle to the database. The database is protected by mutual exclusion during any continuous database access. However, the database cannot be opened for exclusive use, and its state can change dynamically between distinct accesses to the database.

### Determining the Current Usage of COM Port Numbers

After opening the COM port database, a client can determine which COM port numbers are already in use by calling the [**ComDBGetCurrentPortUsage**](https://msdn.microsoft.com/library/windows/hardware/ff546474) routine.

A client typically performs the following tasks:

1.  Calls the routine to determine how many port numbers are currently being arbitrated in the database.

2.  Calls the routine a second time to return information about port number usage in a caller-allocated bit array or byte array, where each bit or byte specifies whether the corresponding port number is in use.

If all port numbers in the database are in use, or there is no suitable port number currently available, the client can resize the database. For more information, see Resizing the COM Port Database.

### Obtaining and Releasing a COM Port Number

A client can obtain a COM port number by calling one of the following routines:

-   [**ComDBClaimNextFreePort**](https://msdn.microsoft.com/library/windows/hardware/ff546469), which claims the lowest available port number.

-   [**ComDBClaimPort**](https://msdn.microsoft.com/library/windows/hardware/ff546472), which attempts to claim a specific port number.

C*laiming* a COM port number in the COM port database logs the port number as "in use".

A client releases a port number by calling the [**ComDBReleasePort**](https://msdn.microsoft.com/library/windows/hardware/ff546477) routine.

### Resizing the COM Port Database

A client can resize the COM port database by calling the [**ComDBResizeDatabase**](https://msdn.microsoft.com/library/windows/hardware/ff546480) routine. A client can only increase the size of the database by integer multiples of 1024. The maximum size of the database is COMDB\_MAX\_PORTS\_ARBITRATED.

 

 




