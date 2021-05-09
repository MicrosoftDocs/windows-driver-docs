---
title: DEBUG\_REQUEST\_SET\_ADDITIONAL\_CREATE\_OPTIONS
description: DEBUG\_REQUEST\_SET\_ADDITIONAL\_CREATE\_OPTIONS
keywords: ["DEBUG_REQUEST_SET_ADDITIONAL_CREATE_OPTIONS Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_REQUEST_SET_ADDITIONAL_CREATE_OPTIONS
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DEBUG\_REQUEST\_SET\_ADDITIONAL\_CREATE\_OPTIONS


The DEBUG\_REQUEST\_SET\_ADDITIONAL\_CREATE\_OPTIONS [**Request**](request.md) operation sets the default process creation options.

**Parameters**

<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
The new default process creation options. The type of the process creation options is [**DEBUG\_CREATE\_PROCESS\_OPTIONS**](/windows-hardware/drivers/ddi/dbgeng/ns-dbgeng-_debug_create_process_options).

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
Not used.

## Remarks

The default process creation options are used by methods [**CreateProcess**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createprocess) and [**CreateProcessAndAttach**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createprocessandattach) which, unlike [**CreateProcess2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createprocess2) and [**CreateProcessAndAttach2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createprocessandattach2), do not specify the full range of process creation options.

The **CreateFlags** field of the [**DEBUG\_CREATE\_PROCESS\_OPTIONS**](/windows-hardware/drivers/ddi/dbgeng/ns-dbgeng-_debug_create_process_options) structure is not used as a default because all process creation operations provide this information.

## <span id="see_also"></span>See also


[**Request**](request.md)

[**DEBUG\_REQUEST\_GET\_ADDITIONAL\_CREATE\_OPTIONS**](debug-request-get-additional-create-options.md)

[**DEBUG\_CREATE\_PROCESS\_OPTIONS**](/windows-hardware/drivers/ddi/dbgeng/ns-dbgeng-_debug_create_process_options)

[**CreateProcess**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createprocess)

[**CreateProcessAndAttach**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createprocessandattach)

 

