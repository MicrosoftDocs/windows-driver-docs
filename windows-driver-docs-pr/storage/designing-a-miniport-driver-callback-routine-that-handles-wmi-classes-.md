---
title: Designing a Miniport Driver Callback Routine that Handles WMI Classes with Data Fields
description: Designing a Miniport Driver Callback Routine that Handles WMI Classes with Data Fields
ms.assetid: 6e08f9c1-e541-4e5f-8c99-f81d5793cc21
keywords: ["WMI SRBs WDK storage , designing callback routines", "callback routines WDK WMI SRBs"]
---

# Designing a Miniport Driver Callback Routine that Handles WMI Classes with Data Fields


## <span id="ddk_designing_a_miniport_driver_callback_routine_that_handles_wmi_clas"></span><span id="DDK_DESIGNING_A_MINIPORT_DRIVER_CALLBACK_ROUTINE_THAT_HANDLES_WMI_CLAS"></span>


This section explains how callback routines must handle input and output data for a WMI class with data fields..

If the WMI class contains data fields, then the WMI tool suite will generate a structure declaration for the data. The structure declaration is apart from any structures that are generated to hold input and output parameters for WMI methods that belong to the class. For more information about the structures that the WMI tool suite generates to handle WMI methods, see Designing a Miniport Driver Callback Routine that Handles WMI Classes with Methods.

For example, suppose we compile the following WMI class definition with **mofcomp** and generate a .h file with **wmimofck**.

```
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

```
typedef struct _HBAFCPBindingEntry
{
  ULONG  Type;
  HBAFCPID  FCPId;
  HBAScsiID  ScsiId;
} HBAFCPBindingEntry, *PHBAFCPBindingEntry;
```

You can cast this structure declaration to the input and output buffers of the SRB when managing input and output data.

Before returning, your callback routine should call [**ScsiPortWmiPostProcess**](https://msdn.microsoft.com/library/windows/hardware/ff564796). This SCSI Port WMI library routine updates the request context with information, such as the status of the request and the size of the return data. For more information about the data stored in the request context, see [**SCSIWMI\_REQUEST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff564946).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Designing%20a%20Miniport%20Driver%20Callback%20Routine%20that%20Handles%20WMI%20Classes%20with%20Data%20Fields%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




