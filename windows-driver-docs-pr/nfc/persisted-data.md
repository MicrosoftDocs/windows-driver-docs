---
title: Persisted data
description: Data persistence is.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 11/15/2022
---

# Persisted data

Data persistence for the registry location is described as follows.

| Location | Contents, Usage, Defaults | Access (if not default) | PII stored? | Is this setting migrated? |
|---|---|---|---|---|
| Device node registry location | NfcRadioTurnedOff, DWORD:</br></br>TRUE: NFC RM is off</br></br>FALSE: NFC RM is on and subject to idle power management | Inherit from the device enum tree, no special ACL set | N/A | No |

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)  
- [NFC class extension (CX) reference](/windows-hardware/drivers/ddi/index)
