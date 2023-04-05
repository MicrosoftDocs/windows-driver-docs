---
title: Common WSD Scan Service operation error codes
description: This article lists error codes that are common to all WSD Scan Service operations.
keywords: ["Common WSD Scan Service Operation Error Codes Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Common WSD Scan Service Operation Error Codes
api_type:
- NA
ms.date: 03/29/2023
---

# Common WSD Scan Service operation error codes

This article lists error codes that are common to all WSD Scan Service operations. If an operation results in multiple errors, the Scan Service should return the most specific error.

- **Wsa:ActionNotSupported**

    The WSD Scan Service returns this fault when a client requests an operation that the Scan Service doesn't support.

    | Fault property | Definition |
    |--|--|
    | \[Code\] | soap:Sender |
    | \[Subcode\] | wsa:ActionNotSupported |
    | \[Reason\] | The \[wsa:action\] can't be processed at the receiver. |
    | \[Detail\] | *The invalid operation name* |

- **InvalidArgs**

    The WSD Scan Service returns this fault when a client sends an invalid argument as part of an operation. The invalid argument could be any of the following:

  - There aren't enough *in* arguments.
  - There are too many *in* arguments.
  - There are no *in* argument by that name.
  - One or more *in* arguments are of the wrong data type.

    | Fault property | Definition |
    |--|--|
    | \[Code\] | soap:Sender |
    | \[Subcode\] | wscn:InvalidArgs |
    | \[Reason\] | At least one input argument is invalid. |
    | \[Detail\] | *The invalid argument* |

- **OperationFailed**

    The WSD Scan Service can return this fault when the current state of the Scan Service prevents invoking the specified operation.

    | Fault property | Definition |
    |--|--|
    | \[Code\] | soap:Receiver |
    | \[Subcode\] | wscn:OperationFailed |
    | \[Reason\] | The service can't perform the requested operation. |
    | \[Detail\] | *None* |

- **ServerErrorTemporaryError**

    The WSD Scan Service returns this fault when the server experiences a temporary error while the scanner is processing the operation. The client can try the unmodified request again at some later point in time with the expectation that the temporary internal error condition might have been cleared. If there's a more specific error that is defined that applies to a temporary error, such as disk full, the Scan Service should return that error code.

    | Fault property | Definition |
    |--|--|
    | \[Code\] | soap:Receiver |
    | \[Subcode\] | wprt:ServerErrorTemporaryError |
    | \[Reason\] | The service had an unexpected error. |
    | \[Detail\] | *None* |

- **ServerErrorInternalError**

    The WSD Scan Service returns this fault when the scanner encounters an unexpected condition that prevents it from fulfilling the request. This error differs from **ServerErrorTemporaryError** in that it implies a more permanent type of internal error and resending the operation will return the same fault.

    | Fault property | Definition |
    |--|--|
    | \[Code\] | soap:Receiver |
    | \[Subcode\] | wscn:ServerErrorInternalError |
    | \[Reason\] | The service had an unexpected error. |
    | \[Detail\] | *None* |
