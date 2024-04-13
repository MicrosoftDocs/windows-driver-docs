---
title: SetCHAPSharedSecret
description: SetCHAPSharedSecret
ms.date: 10/17/2018
---

# SetCHAPSharedSecret


The **SetCHAPSharedSecret** method establishes the shared secret for the initiator to use when it verifies the target's response to the initiator's challenge.

The initiator uses two different shared secrets to implement the challenge handshake authentication protocol (CHAP):

-   The **SetCHAPSharedSecret** method establishes the shared secret that the initiator uses to verify the target's response to the initiator's challenge.

-   The [LoginToTarget](logintotarget.md) method establishes the shared secret that the initiator uses to generate the CHAP response to a target's challenge.

The **SetCHAPSharedSecret** WMI method belongs to the unpublished [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md). For a description of the parameters of the **SetCHAPSharedSecret** method, see the member descriptions for the [**SetCHAPSharedSecret\_IN**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_setchapsharedsecret_in) and [**SetCHAPSharedSecret\_OUT**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_setchapsharedsecret_out) structures.

Miniport drivers that implement the MSiSCSI\_Operations WMI class are not required to support **SetCHAPSharedSecret**.

 

