---
title: Design Miniport Callback Routine to Handle WMI Classes
description: Designing a Miniport Driver Callback Routine that Handles WMI Classes with Data Fields
ms.assetid: 6e08f9c1-e541-4e5f-8c99-f81d5793cc21
keywords:
- WMI SRBs WDK storage , designing callback routines
- callback routines WDK WMI SRBs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Designing a Miniport Driver Callback Routine that Handles WMI Classes with Data Fields


## <span id="ddk_designing_a_miniport_driver_callback_routine_that_handles_wmi_clas"></span><span id="DDK_DESIGNING_A_MINIPORT_DRIVER_CALLBACK_ROUTINE_THAT_HANDLES_WMI_CLAS"></span>


This section explains how callback routines must handle input and output data for a WMI class with data fields..

If the WMI class contains data fields, then the WMI tool suite will generate a structure declaration for the data. The structure declaration is apart from any structures that are generated to hold input and output parameters for WMI methods that belong to the class. For more information about the structures that the WMI tool suite generates to handle WMI methods, see Designing a Miniport Driver Callback Routine that Handles WMI Classes with Methods.

For example, suppose we compile the following WMI class definition with **mofcomp** and generate a .h file with **wmimofck**.

```cpp
class HBAFCPBindingEntry
{
  [HBAType("HBA_FCPBINDINGTYPE"),
   Values{"TO_D_ID", "TO_WWN", "TO_OTHER"},
   ValueMap{"0", "1", "2"},
   WmiDataId(1)
  ]
  uint32  Type;
  [HBAType("HBA_FCID"),
   WmiDataId(2)
  ]
  HBAFCPID  FCPId;
  [HBAType("HBA_FCPSCSIENTRY"),
   WmiDataId(3)
  ]
  HBAScsiID  ScsiId;
};
```

The resulting .h file will contain the following structure declaration.

```cpp
typedef struct _HBAFCPBindingEntry
{
  ULONG  Type;
  HBAFCPID  FCPId;
  HBAScsiID  ScsiId;
} HBAFCPBindingEntry, *PHBAFCPBindingEntry;
```

You can cast this structure declaration to the input and output buffers of the SRB when managing input and output data.

Before returning, your callback routine should call [**ScsiPortWmiPostProcess**](https://msdn.microsoft.com/library/windows/hardware/ff564796). This SCSI Port WMI library routine updates the request context with information, such as the status of the request and the size of the return data. For more information about the data stored in the request context, see [**SCSIWMI\_REQUEST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff564946).

 

 




