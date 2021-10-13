---
title: WSK_CLIENT
description: This topic describes the WSK_CLIENT data type for WSK applications.
keywords:
- WSK_CLIENT, WDK WSK_CLIENT network drivers
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WSK_CLIENT

The WSK_CLIENT data type defines the WSK subsystem's binding context for its attachment to a WSK application.

```c++
typedef PVOID PWSK_CLIENT;
```

**PWSK_CLIENT**  
The contents of the **WSK_CLIENT** structure are opaque to a WSK application.

## Remarks

When a WSK application calls the [WskCaptureProviderNPI](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskcaptureprovidernpi) function, the WSK subsystem returns a pointer to a WSK_CLIENT structure to the WSK application by means of the *WskProviderNpi* parameter. The WSK subsystem uses this structure to track the state of the binding between the WSK application and the WSK subsystem. A WSK application passes this pointer as a parameter to all the functions in [WSK_PROVIDER_DISPATCH](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_dispatch) ([WskControlClient](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client), [WskSocket](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket), and [WskSocketConnect](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket_connect)).

For more information, see [Registering a Winsock Kernel Application](registering-a-winsock-kernel-application.md).

## Requirements

**Version**: Available in Windows Vista and later versions of the Windows operating systems.

**Header**: Wsk.h (include Wsk.h)


## See also

[WskCaptureProviderNPI](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskcaptureprovidernpi)  
[WskControlClient](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client)  
[WskSocket](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket)  
[WskSocketConnect](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket_connect)  
[WSK_PROVIDER_DISPATCH](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_dispatch)
