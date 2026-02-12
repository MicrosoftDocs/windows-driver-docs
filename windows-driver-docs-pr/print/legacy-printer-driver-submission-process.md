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

### All printer driver submissions are blocked by default

Every submission that targets a print driver class is automatically halted during intake and undergoes a review. This action applies to:

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

The justification document is a JSON file that can be created using [this schema.](#schema) The DriverExceptionDocGenerator tool will be available in the near future to automatically generate the schema.

Partners may include extra supporting materials if needed, such as security disclosures, Mopria analysis, roadmaps, model comparisons. These supporting materials help the reviewers validate exception claims.

### File packaging requirements

- WHQL submissions:
The justification JSON and any supporting documents must be placed inside the HLK package in the Supplemental folder before uploading.- Attestation submissions:
Because Attestation packages don't have a Supplemental folder, the justification JSON and supporting documentation must be placed in the driver folder itself.

### These documents aren't signed

Justification content isn't referenced in the INF, and therefore:

- It isn't signed,
- It isn't included in the driver package installed on client devices.

## Exceptions Allowed in 2026

Beginning January 15, 2026, the following exception categories apply:

### New Drivers

New printer driver submissions will only be signed/published if they meet one of these criteria:

- Device can't support Mopria
- Device is a Fax device
- Adding ARM64 version
- Target Windows 10 22H2 or earlier
- Target Windows Server 2022 or earlier

### Driver Updates

Existing driver updates are only signed and published if they:

- Don't add new HWIDs
- Don't add new functionality
- Provide the submission id of the existing driver it is replacing/updating
- And meet one of the following criteria:
  - Provide a security update
  - Device is a Fax device
  - Add an ARM64 version
  - Target Windows 10 22H2 or earlier
  - Target Windows Server 2022 or earlier

## Generating the Justification Document

### DriverExceptionDocGenerator Tool (Coming Soon)

The justification document must follow the [schema provided.](#schema) In the future, Microsoft will provide a dedicated tool to help partners prepare the justification JSON. This tool, named **DriverExceptionDocGenerator**, will be available as a command‑line utility and will guide partners through the process of generating a valid justification document.

#### Tool Capabilities

- Run interactively (prompt‑driven)
- Run non‑interactively by providing parameters
- Produces a JSON document aligned to the Microsoft schema
- Validates field formatting and required sections

#### When to use DriverExceptionDocGenerator

Partners should use this tool for every printer driver submission, including:

- New printer drivers
- Driver updates
- Security updates
- Architecture additions (for example, ARM64)

## Information Required in the Justification JSON

The justification JSON must follow the [schema provided.](#schema). At a high level, partners must provide:

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

The Windows team recognizes that a small set of printers—typically older mechanical designs or specialized devices—can't feasibly support Mopria due to:

- Hardware protocol limitations.
- Lack of firmware extensibility.
- Embedded controller constraints.
- Highly specialized hardware

What partners must provide

Partners must supply **technical evidence**, not general statements. Required elements include:

- A clear description of why the device can't meet Mopria transport and service requirements.
- Hardware/firmware limitations preventing compliance.
- Confirmation that the partner evaluated, and ruled out, firmware updates, controller upgrades, or protocol layer shims.
- Future roadmap (if any) describing when Mopria compliance may be feasible.

Good example of this justification

"The device’s controller uses a fixed‑function print pipeline that can't be updated to IPP. No extensibility or firmware update path exists. Supporting Mopria would require redesigning the ASIC. Replacement models launching in FY27 will support Mopria."

#### Exception Type 2: ARM64Addition

What this means

The partner is adding an ARM64 version of an existing or new driver.

Why Microsoft allows this exception

Microsoft is accelerating ARM64 adoption across Windows, and exceptions allow partners to:

- Ship ARM64 parity for existing devices.
- Support SoC‑based hardware where modern print pipelines may not yet be adopted.

What partners must provide

- Confirmation the ARM64 version is functionally equivalent to existing architectures.
- Explanation why a modern IPP‑based implementation isn't yet viable for this architecture.
- A roadmap for eventual migration to the modern platform.

> [!IMPORTANT]
> Adding/Updating a driver to support ARM64 has the following restrictions:
>
>For a New Driver
>
>- This pathway is intended for a new printer driver that is only for ARM64. If an existing x86 or AMD64 driver already exists, then this driver is a 'Driver Update' scenario where ARM64 support is being added.
>- If the driver also contains support for x86 or AMD64 in addition to ARM64 and is marked as 'New Driver' it will be rejected.
>
>For a Driver Update
>
>- The previous submission id information must be populated with the previous driver that targeted x86 or AMD64.
>- The ARM64 driver must have a matching set of HWIDs/Compatible Ids to the previous driver.

#### Exception Type 3: Windows10Only

What this means

The driver is intended only for Windows 10 Version 22H2 (build 19045), Windows Server 2022 (build 20348), or earlier versions of Windows/Windows Server.

Why Microsoft allows this exception

Windows 10 (22H2)/Windows Server 2022 remains in support, but don't include all the necessary platform improvements required for full modern print stack parity. Thus some scenarios still require legacy V3/V4 drivers.

What partners must provide

- Confirmation that the driver targets only Windows 10 22H2/Windows Server 2022 and isn't intended for Windows 11.
- Explanation of why IPP‑based solutions can't support the device on Windows 10/Windows Server 2022.
- Evidence that the partner isn't using this exception to bypass Windows 11 requirements.

> [!IMPORTANT]
> If approved for this exception the partner MUST only select Windows 10/Windows Server 2022 (or earlier) versions of Windows for publishing. If the partner tries to ship the same package for both Windows 10/Windows Server 2022 and Windows 11/Windows Server 2025 (or later), the exception is no longer valid, and the driver is blocked from being signed and published.

#### Exception Type 4: FaxDriver

What this means

The partner is adding or updating a driver for a fax device.

Why Microsoft allows this exception

Windows doesn't distinguish between a printer driver and a fax driver at an INF class level and therefore all fax drivers are subject to the same restrictions as printer drivers. However, IPP FaxOut support is still rolling out so some fax scenarios will still require a legacy V3/V4 driver.

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
> Security updates can't introduce:
>
> - New HWIDs
> - Functional enhancements not related to the security fix.

#### Exception Type 6: Other

What this means

This exception is a catch‑all category for rare, well‑justified, technically compelling exceptions not covered elsewhare in this document.

Why Microsoft allows this exception

There may be edge‑case scenarios in:

- Regulatory environments

What partners must provide

- A detailed custom justification explaining the need.
- Supporting evidence—technical documentation, regulatory requirements, telemetry insights, etc.
- Explanation of why none of the other exception categories apply.

Examples of acceptable "Other" justifications

- Devices bound to government‑mandated print protocols that aren't IPP‑based.
- Medical or industrial printers where firmware can't be updated for several years due to certification cycles.

### Partner Submission Checklist

Before submitting, partners should ensure:

✔ They have generated a valid justification JSON

Use DriverExceptionDocGenerator to generate the JSON file.

✔ Additional supporting documents (if needed) are included

Especially for security or Mopria documentation.

✔ Files are placed correctly:

- WHQL → HLK package → /Supplemental
- Attestation → driver package root folder

✔ If "DriverUpdate": PreviousSubmissionId is included

Missing the PreviousSubmissionId causes immediate rejection.

✔ No new HWIDs for DriverUpdate submissions

Mismatch results in automatic rejection.

### FAQ

**What happens if I submit without a justification document?**

The submission is automatically blocked and rejected during manual review.

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

3       │    ├─ DriverException.json

4       │    └─ SupportingDocument.docx

## Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://microsoft.com/schemas/driver-exception-document.json",
  "title": "Driver Exception Document",
  "description": "Schema for driver exception requests for deprecated V3/V4 printer drivers",
  "type": "object",
  "required": [
    "Version",
    "SubmissionDate",
    "PartnerInformation",
    "DriverDetails",
    "SubmissionType",
    "ExceptionJustification"
  ],
  "properties": {
    "Version": {
      "type": "string",
      "description": "Schema version number",
      "const": "1.0"
    },
    "SubmissionDate": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp of submission (UTC)",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
    },
    "PartnerInformation": {
      "type": "object",
      "description": "Partner contact information",
      "required": [
        "CompanyName",
        "ContactName",
        "ContactEmail"
      ],
      "properties": {
        "CompanyName": {
          "type": "string",
          "description": "Partner company name",
          "minLength": 1
        },
        "ContactName": {
          "type": "string",
          "description": "Contact person name",
          "minLength": 1
        },
        "ContactEmail": {
          "type": "string",
          "format": "email",
          "description": "Contact email address",
          "minLength": 1
        }
      },
      "additionalProperties": false
    },
    "DriverDetails": {
      "type": "object",
      "description": "Driver package details",
      "required": [
        "TargetModels",
        "Architectures",
        "DriverVersion",
        "ChangeOverview"
      ],
      "properties": {
        "TargetModels": {
          "type": "array",
          "description": "List of target printer models",
          "minItems": 1,
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "Architectures": {
          "type": "array",
          "description": "Architectures targeted by the driver package",
          "minItems": 1,
          "items": {
            "type": "string",
            "enum": ["x86", "x64", "arm64"],
            "description": "Architecture (x64 also accepts amd64 in input, normalized to x64)"
          }
        },
        "DriverVersion": {
          "type": "string",
          "description": "Driver version number",
          "minLength": 1
        },
        "ChangeOverview": {
          "type": "string",
          "description": "Overview of changes in this driver submission",
          "minLength": 1
        }
      },
      "additionalProperties": false
    },
    "SubmissionType": {
      "type": "string",
      "description": "Type of driver submission",
      "enum": [
        "NewDriver",
        "DriverUpdate"
      ]
    },
    "DriverUpdateDetails": {
      "type": "object",
      "description": "Additional details required for driver updates (required when SubmissionType is DriverUpdate)",
      "required": [
        "PreviousSubmissionId",
        "AttestNoNewHardwareIds"
      ],
      "properties": {
        "PreviousSubmissionId": {
          "type": "string",
          "description": "Previous submission identifier",
          "minLength": 1
        },
        "AttestNoNewHardwareIds": {
          "type": "boolean",
          "description": "Attestation that no new hardware IDs are being added"
        }
      },
      "additionalProperties": false
    },
    "ExceptionJustification": {
      "type": "object",
      "description": "Justification for the driver exception",
      "required": [
        "ExceptionType",
        "ImpactOnUsers"
      ],
      "properties": {
        "ExceptionType": {
          "type": "string",
          "description": "Type of exception being requested",
          "enum": [
            "CannotSupportMopria",
            "ARM64Addition",
            "Windows10Only",
            "FaxDriver",
            "SecurityVulnerability",
            "Other"
          ]
        },
        "ImpactOnUsers": {
          "type": "string",
          "description": "Description of impact on end users",
          "minLength": 1
        },
        "CustomJustification": {
          "type": "string",
          "description": "Custom justification (required when ExceptionType is Other)",
          "minLength": 1
        },
        "SecurityDetails": {
          "type": "object",
          "description": "Security vulnerability details (required when ExceptionType is SecurityVulnerability)",
          "required": [
            "CveReference"
          ],
          "properties": {
            "CveReference": {
              "type": "string",
              "description": "CVE reference identifier",
              "pattern": "^CVE-\\d{4}-\\d{4,}$"
            },
            "VulnerabilityDescription": {
              "type": "string",
              "description": "Detailed description of the vulnerability"
            }
          },
          "additionalProperties": false
        },
        "MopriaDetails": {
          "type": "object",
          "description": "Mopria exception details (required when ExceptionType is CannotSupportMopria)",
          "required": [
            "TechnicalReason",
            "FutureRoadmap"
          ],
          "properties": {
            "TechnicalReason": {
              "type": "string",
              "description": "Technical reason why Mopria cannot be supported",
              "minLength": 1
            },
            "FutureRoadmap": {
              "type": "string",
              "description": "Future roadmap for Mopria support",
              "minLength": 1
            }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "ExceptionType": {
                "const": "Other"
              }
            }
          },
          "then": {
            "required": [
              "CustomJustification"
            ]
          }
        },
        {
          "if": {
            "properties": {
              "ExceptionType": {
                "const": "SecurityVulnerability"
              }
            }
          },
          "then": {
            "required": [
              "SecurityDetails"
            ]
          }
        },
        {
          "if": {
            "properties": {
              "ExceptionType": {
                "const": "CannotSupportMopria"
              }
            }
          },
          "then": {
            "required": [
              "MopriaDetails"
            ]
          }
        }
      ]
    }
  },
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "SubmissionType": {
            "const": "DriverUpdate"
          }
        }
      },
      "then": {
        "required": [
          "DriverUpdateDetails"
        ]
      }
    }
  ]
}
```
