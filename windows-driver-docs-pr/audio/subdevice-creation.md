---
title: Subdevice Creation
description: Subdevice Creation
keywords:
- audio adapters WDK , subdevices
- adapter drivers WDK audio , subdevices
- subdevices WDK audio
ms.date: 04/20/2017
---

# Subdevice Creation


## <span id="subdevice_creation"></span><span id="SUBDEVICE_CREATION"></span>


The term *subdevice* is used to describe the binding of the four components that are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Component</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Miniport object</p></td>
<td align="left"><p>An object that exposes the miniport driver's IMiniport<em>Xxx</em> interface</p></td>
</tr>
<tr class="even">
<td align="left"><p>Port object</p></td>
<td align="left"><p>An object that exposes the port driver's IPort<em>Xxx</em> interface</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Resource list object</p></td>
<td align="left"><p>An object containing a list of adapter driver resources that are assigned to the subdevice</p></td>
</tr>
<tr class="even">
<td align="left"><p>Reference string</p></td>
<td align="left"><p>A name added to the device path name to specify a subdevice during filter creation</p></td>
</tr>
</tbody>
</table>

 

A subdevice's IMiniport*Xxx* and IPort*Xxx* interfaces inherit from base interfaces [IMiniport](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiport) and [IPort](/windows-hardware/drivers/ddi/portcls/nn-portcls-iport), respectively.

The PortCls system driver does not distinguish between the port driver and the miniport driver. It simply requires an object, such as the port object, with an interface that can handle system-generated requests.

Similarly, PortCls is not directly involved in managing resources. It only needs to bind the request handler (the port driver) to a resource list. The adapter driver is responsible for binding the port, miniport, and resource list objects together.

The following code example shows how the adapter driver performs these actions:

```cpp
  //
  // Instantiate the port by calling a function supplied by PortCls.
  //
  PPORT    port;
  NTSTATUS ntStatus = PcNewPort(&port, PortClassId);

  if (NT_SUCCESS(ntStatus))
  {
      PUNKNOWN miniport;
      //
      // Create the miniport object.
      //
      if (MiniportCreate)   // a function to create a proprietary miniport
      {
          ntStatus = MiniportCreate(&miniport,
                                    MiniportClassId, NULL, NonPagedPool);
      }
      else   // Ask PortCls for one of its built-in miniports.
      {
          ntStatus = PcNewMiniport((PMINIPORT*)&miniport,
                                   MiniportClassId);
      }

      if (NT_SUCCESS(ntStatus))
      {
          //
          // Bind the port, miniport, and resources.
          //
          ntStatus = port->Init(DeviceObject,
                                Irp, miniport, UnknownAdapter, ResourceList);
          if (NT_SUCCESS(ntStatus))
          {
              //
              // Hand the port driver and the reference
              // string to PortCls.
              //
              ntStatus = PcRegisterSubdevice(DeviceObject,
                                             Name, port);
          }

          //
          // We no longer need to reference the miniport driver.
          // Either the port driver now references it,
          // or binding failed and it should be deleted.
          //
          miniport->Release();
      }

      //
      // Release the reference that existed when PcNewPort() gave us
      // the pointer in the first place. This reference must be released
      // regardless of whether the binding of the port and miniport
      // drivers succeeded.
      //
      port->Release();
  }
```

For information about the PortCls function calls in the preceding code example, see [**PcNewPort**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewport), [**PcNewMiniport**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewminiport), and [**PcRegisterSubdevice**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregistersubdevice).

 

