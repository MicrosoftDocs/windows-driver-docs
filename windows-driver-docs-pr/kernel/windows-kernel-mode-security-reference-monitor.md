---
title: Windows Kernel-Mode Security Reference Monitor
description: Learn about the Windows Security Reference Monitor and how to use its routines for access control in kernel-mode drivers.
ms.date: 09/24/2025
ms.topic: concept-article
---

# Windows Kernel-Mode Security Reference Monitor

Security is a critical consideration when developing device drivers, particularly drivers operating in kernel mode with elevated privileges. Before any action can take place, the operating system must ensure that the action doesn't violate system security policy. Device drivers need mechanisms to control which processes and users can access their devices and what operations they're permitted to perform.

The Windows Security Reference Monitor (SRM) is a core kernel-mode component of the Windows security architecture that enforces access control policies throughout the operating system. It validates every request to access system objects and ensures that only authorized entities can perform specific operations.

## Key functions of the Security Reference Monitor

The SRM performs several functions to maintain system security:

- Access control enforcement: Validates every request to access system objects such as files, registry keys, and processes.
- Security policy implementation: Enforces system-wide security policies and implements the principle of least privilege.
- Audit and logging: Generates security audit events and tracks security-relevant activities for compliance and forensics.

## Architecture components

The SRM works with several key data structures and components to enforce security policies.

### Security descriptors

[Security descriptors](security-descriptors.md) are data structures that contain security information for objects.

Information in a security descriptor is stored in an [access control list (ACL)](../ifs/access-control-list.md). Windows uses ACLs to determine which objects have what security.

## Security reference monitor routines

The SRM provides routines for your driver to work with access control. Routines that provide a direct interface to the SRM are prefixed with the letters *Se*. Common SRM routines include:

- [**SeAccessCheck**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck): Performs access validation against a security descriptor.
- [**SePrivilegeCheck**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seprivilegecheck): Checks if a token has specific privileges.
- [**SeSinglePrivilegeCheck**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-sesingleprivilegecheck): Checks for a single privilege in an access token in the context of the current thread.
- [**SeTokenType**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-setokentype): Determines whether a token is a primary or impersonation token.

Declarations for *Se* functions and related entities can be found in various WDK headers, including [*ntifs.h*](/windows-hardware/drivers/ddi/ntifs/) and [*wdm.h*](/windows-hardware/drivers/ddi/wdm/).

## Driver implementation scenarios

Device drivers commonly use the SRM in several scenarios to implement proper access controls.

### Device access control

Drivers can control which users can access specific hardware devices:

- Check user permissions before allowing device operations.
- Implement different access levels for different types of users.
- Restrict administrative operations to privileged users.

### Operation validation

Drivers can ensure only authorized processes can perform specific device operations:

- Validate security context before processing I/O requests.
- Check for specific privileges required for sensitive operations.
- Implement custom security policies for device-specific functions.

### Security context management

Drivers working with impersonation and different security contexts can:

- Handle impersonation tokens appropriately.
- Switch between different security contexts as needed.
- Maintain security boundaries between different user sessions.

## Security principles

The SRM implements fundamental security principles that are essential for maintaining system integrity.

### Complete mediation

Every access attempt must go through the reference monitor:

- No exceptions or bypass mechanisms exist.
- Ensures consistent security policy enforcement across all system components.
- Prevents unauthorized access through alternative code paths.

### Least privilege

The reference monitor helps implement the principle of least privilege:

- Users and processes should have only the minimum permissions needed.
- Helps minimize potential damage from security breaches.
- Implemented through careful ACL configuration and privilege management.
