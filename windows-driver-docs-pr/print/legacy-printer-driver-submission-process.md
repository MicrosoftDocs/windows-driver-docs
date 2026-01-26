---
title: Legacy Printer Driver Submission Process
description: Defines the justification documentation required with each new printer driver submission.
keywords:
- print devices WDK
- print WDK See printer driver
- print WDK See printing
ms.date: 01/26/2026
ms.topic: release-notes
---

# Legacy Printer Driver Submission Process

Effective **January 15th, 2026**, Microsoft implemented the next phase of the [Windows print driver deprecation plan](end-of-servicing-plan-for-third-party-printer-drivers-on-windows.md). Under this policy, **all printer driver submissions—both WHQL and Attestation—will be blocked by default** and will instead undergo a manual review process.
To ensure a consistent and transparent process, print partners are now required to provide a **justification documentation** with **each** new printer driver submission as outlined in this topic.

## What Partners Should Expect

### All printer driver submissions will be blocked by default

Every submission that targets a print driver class will be automatically halted during intake and undergo a review. This applies to:

- WHQL driver submissions
- Attestation submissions

### All submissions must include a justification document

Partners are required to provide a Driver Exception Justification Document describing:

- Submission type (New Driver or Driver Update)
- Details about the driver package
- Which exception category the submission falls into
- Why the exception is required

> [!NOTE]
> This justification is required for every driver in a submission and for every submission, even when the partner believes the submission already qualifies under an exception.

### Justification document format

The justification document is a JSON file that will be generated using the new DriverExceptionDocGenerator tool.

Partners may include extra supporting materials if needed, such as security disclosures, Mopria analysis, roadmaps, model comparisons. These supporting materials help the reviewers validate exception claims.

### File packaging requirements

- WHQL submissions:
The justification JSON and any supporting documents must be placed inside the HLK package in the Supplemental folder before uploading.- Attestation submissions:
Because Attestation packages do not have a Supplemental folder, the justification JSON and supporting documentation must be placed in the driver folder itself.

### These documents are not signed

Justification content is not referenced in the INF, and therefore:

- It is not signed,
- It is not included in the driver package installed on client devices.

## Exceptions Allowed in 2026

Beginning January 15, 2026, the following exception categories apply:

### New Drivers

New printer driver submissions will only be signed/published if they meet one of these criteria:

- Device cannot support Mopria
- Device is a Fax device
- Adding ARM64 version
- Target Windows 10 22H2 or earlier
- Target Windows Server 2022 or earlier

### Driver Updates

Existing driver updates will only be signed/published if they do not add new HWIDs, do not add new functionality, provide the submission id of the existing driver it is replacing/updating, and meet one of the following criteria:

- Provide a security update
- Device is a Fax device
- Add an ARM64 version
- Target Windows 10 22H2 or earlier
- Target Windows Server 2022 or earlier

## Generating the Justification Document

### DriverExceptionDocGenerator Tool

Microsoft provides a dedicated tool to help partners prepare the justification JSON:

### Tool Capabilities

- Run interactively (prompt‑driven)
- Run non‑interactively by providing parameters
- Produces a JSON document aligned to the Microsoft schema
- Validates field formatting and required sections

### When to use DriverExceptionDocGenerator

Partners should use this tool for every printer driver submission, including:

- New printer drivers
- Driver updates
- Security updates
- Architecture additions (e.g., ARM64)

## Information Required in the Justification JSON

The justification JSON must follow the schema provided (omitted here for brevity but included in your partner enablement package). At a high level, partners must provide:

### Submission Metadata

- Version (fixed: 1.0)
- SubmissionDate (ISO 8601, UTC)

### Partner Information

- Company name
- Contact name
- Contact email

### Driver Details

- Target models
- Driver version
- Overview of changes

### Submission Types

- NewDriver
- DriverUpdate
  - If DriverUpdate, partner must provide:
    - PreviousSubmissionId
    - Confirmation that no new HWIDs are added

### Exception Justification

The partner must request and justify one exception type.

#### Exception Type 1: CannotSupportMopria

What this means

A partner may claim this exception when a printer **cannot support the Mopria standard**, which is the baseline for the modern Windows print platform.

Why Microsoft allows this exception

The Windows team recognizes that a small set of printers—typically older mechanical designs or specialized devices—cannot feasibly support Mopria due to:

- Hardware protocol limitations.
- Lack of firmware extensibility.
- Embedded controller constraints.
- Highly specialized hardware

What partners must provide

Partners must supply **technical evidence**, not general statements. Required elements include:

- A clear description of why the device cannot meet Mopria transport and service requirements.
- Hardware/firmware limitations preventing compliance.
- Confirmation that the partner evaluated, and ruled out, firmware updates, controller upgrades, or protocol layer shims.
- Future roadmap (if any) describing when Mopria compliance may be feasible.

Good example of this justification

“The device’s controller uses a fixed‑function print pipeline that cannot be updated to IPP. No extensibility or firmware update path exists. Supporting Mopria would require redesigning the ASIC. Replacement models launching in FY27 will support Mopria.”

#### Exception Type 2: ARM64Addition

What this means

The partner is adding an ARM64 version of an existing or new driver.

Why Microsoft allows this exception

Microsoft is accelerating ARM64 adoption across Windows, and exceptions allow partners to:

- Ship ARM64 parity for existing devices.
- Support SoC‑based hardware where modern print pipelines may not yet be adopted.

What partners must provide

- Confirmation the ARM64 version is functionally equivalent to existing architectures.
- Explanation why a modern IPP‑based implementation is not yet viable for this architecture.
- A roadmap for eventual migration to the modern platform.

> [!IMPORTANT]
> Adding/Updating a driver to support ARM64 has the following restrictions:
>
>For a New Driver
>
>- This pathway is intended for a new printer driver that is only for ARM64. If an existing x86 or AMD64 driver already exists, then this would be a ‘Driver Update’ scenario where ARM64 support is being added.
>- If the driver also contains support for x86 or AMD64 in addition to ARM64 and is marked as ‘New Driver’ it will be rejected.
>
>For a Driver Update
>
>- The previous submission id information must be populated with the previous driver that targeted x86 or AMD64.
>- The ARM64 driver must have a matching set of HWIDs/Compatible Ids to the previous driver.

#### Exception Type 3: Windows10Only

What this means

The driver is intended only for Windows 10 Version 22H2 (build 19045), Windows Server 2022 (build 20348), or earlier versions of Windows/Windows Server.

Why Microsoft allows this exception

Windows 10 (22H2)/Windows Server 2022 remains in support, but do not include all the necessary platform improvements required for full modern print stack parity. Thus some scenarios still require legacy V3/V4 drivers.

What partners must provide

- Confirmation that the driver targets only Windows 10 22H2/Windows Server 2022 and is not intended for Windows 11.
- Explanation of why IPP‑based solutions cannot support the device on Windows 10/Windows Server 2022.
- Evidence that the partner is not using this exception to bypass Windows 11 requirements.

> [!IMPORTANT]
> If approved for this exception the partner MUST only select Windows 10/Windows Server 2022 (or earlier) versions of Windows for publishing. If the partner tries to ship the same package for both Windows 10/Windows Server 2022 and Windows 11/Windows Server 2025 (or later), the exception is no longer valid, and the driver will be blocked from being signed and published.

#### Exception Type 4: FaxDriver

What this means

The partner is adding or updating a driver for a fax device.

Why Microsoft allows this exception

Windows does not distinguish between a printer driver and a fax driver at an INF class level and therefore all fax drivers are subject to the same restrictions as printer drivers. However, IPP FaxOut support is still rolling out so some fax scenarios will still require a legacy V3/V4 driver.

What partners must provide

- Confirmation that the driver **targets a fax device**.
- Future roadmap (if any) describing when Mopria compliance may be feasible.

> [!IMPORTANT]
> If approved for this exception the driver MUST only target a fax device. If the partner tries to target a printer device with the package, the exception is no longer valid, and the driver will be blocked from being signed and published.

#### Exception Type 5: SecurityVulnerability

What this means

The submission is an update that fixes a security vulnerability in an existing driver.

Why Microsoft allows this exception

Microsoft prioritizes the security of the Windows ecosystem. Securing existing deployments on Windows Update requires allowing:

- Replacement binaries.
- Emergency fixes.
- Urgent vulnerability mitigations.

This category is specifically recognized for driver updates.
What partners must provide

- A valid CVE reference.
- A clear vulnerability description (attack surface, risk severity, affected components).
- Explanation of why fixing the vulnerability requires updating the V3/V4 driver rather than replacing it with IPP.

> [!IMPORTANT]
> Security updates cannot introduce:
>
> - New HWIDs
> - Functional enhancements not related to the security fix.

#### Exception Type 6: Other

What this means

This is a catch‑all category for rare, well‑justified, technically compelling exceptions not covered above.

Why Microsoft allows this exception

There may be edge‑case scenarios in:

- Regulatory environments

What partners must provide

- A detailed custom justification explaining the need.
- Supporting evidence—technical documentation, regulatory requirements, telemetry insights, etc.
- Explanation of why none of the other exception categories apply.

Examples of acceptable “Other”

- Devices bound to government‑mandated print protocols that are not IPP‑based.
- Medical or industrial printers where firmware cannot be updated for several years due to certification cycles.

### Partner Submission Checklist

Before submitting, partners should ensure:
✔ A valid justification JSON has been generated

Use DriverExceptionDocGenerator to generate the JSON file.

✔ Additional supporting documents (if needed) are included

Especially for security or Mopria documentation.

✔ Files are placed correctly:

- WHQL → HLK package → /Supplemental
- Attestation → driver package root folder

✔ If “DriverUpdate”: PreviousSubmissionId is included

Missing this will cause immediate rejection.

✔ No new HWIDs for DriverUpdate submissions

Mismatch results in automatic rejection.

### FAQ

**What happens if I submit without a justification document?**

The submission will be automatically blocked and rejected during manual review.

**Do I need to use the DriverExceptionDocGenerator tool?**

Yes. It ensures schema compliance and reduces submission rejection risk.

**Can a DriverUpdate add new HWIDs?**

No. Any new HWIDs result in automatic rejection.

**Where do I place JSON for Attestation submissions?**

Place it directly inside the driver folder.

### Example Folder Structures

WHQL Example

1     HLKPackage/

2       ├─ HLKFiles/...

3       ├─ Supplemental/

4       │    ├─ DriverException.json

5       │    └─ AdditionalDocumentation.pdf

Attestation Example

1     DriverSubmission/

2       ├─ DriverFiles/...

3       ├─ DriverException.json

4       └─ SupportingDocument.docx
