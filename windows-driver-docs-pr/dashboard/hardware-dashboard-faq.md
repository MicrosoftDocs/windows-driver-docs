---
title: Hardware dashboard FAQ
description: This article provides answers to frequently asked questions about the Windows Hardware Dev Center dashboard.
ms.assetid: AA3D1147-7015-4D21-84A6-D127F57DDC97
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware dashboard FAQ


This article provides answers to frequently asked questions about the Windows Hardware Dev Center dashboard.

## <span id="How_do_I_contact_Hardware_Dev_Center_Dashboard_Support_"></span><span id="how_do_i_contact_hardware_dev_center_dashboard_support_"></span><span id="HOW_DO_I_CONTACT_HARDWARE_DEV_CENTER_DASHBOARD_SUPPORT_"></span>How do I contact Hardware Dev Center Dashboard Support?

If you are having problems accessing the Dashboard or need Dashboard Support please open a support ticket here: https://developer.microsoft.com/windows/support.  Select **Contact us**,  **Dashboard issue**, and then **Hardware submissions & signing (all OS version)** from the dropdown.


## <span id="Can_I_associate_multiple_certificates_with_a_dashboard_account_"></span><span id="can_i_associate_multiple_certificates_with_a_dashboard_account_"></span><span id="CAN_I_ASSOCIATE_MULTIPLE_CERTIFICATES_WITH_A_DASHBOARD_ACCOUNT_"></span>Can I associate multiple certificates with a dashboard account?


One organization can associate multiple certificates with its dashboard account. Your submissions must be signed with any one of those certificates.

There is no restriction on the number of certificates (both EV and Standard) associated with your organization.

## <span id="What_agreements_need_to_be_signed_"></span><span id="what_agreements_need_to_be_signed_"></span><span id="WHAT_AGREEMENTS_NEED_TO_BE_SIGNED_"></span>What agreements need to be signed?


The following agreements can be signed as part of the registration process.

> [!NOTE]
> Signing the Windows Hardware Compatibility Program Test Agreement is a requirement for all registrations. All other agreements are optional unless you are using features or assets in the other associated agreements. 

-   Windows Hardware Compatibility Program Test Agreement (ver 2.0)

-   Logo License Agreement for Hardware (ver 2017)

-   UEFI Addendum

-   Windows Error Reporting (WER) Agreement (ver 1.3)

## <span id="How_do_I_add_additional_users_or_grant_additional_roles_to_users_in_my_company_"></span><span id="how_do_i_add_additional_users_or_grant_additional_roles_to_users_in_my_company_"></span><span id="HOW_DO_I_ADD_ADDITIONAL_USERS_OR_GRANT_ADDITIONAL_ROLES_TO_USERS_IN_MY_COMPANY_"></span>How do I add additional users or grant additional roles to users in my company?


See [Managing User Roles](managing-user-roles.md) for more information.

## <span id="Managing_submissions"></span><span id="managing_submissions"></span><span id="MANAGING_SUBMISSIONS"></span>Managing submissions


### <span id="What__is_the_hardware_certification_submission_processing_time_"></span><span id="what__is_the_hardware_certification_submission_processing_time_"></span><span id="WHAT__IS_THE_HARDWARE_CERTIFICATION_SUBMISSION_PROCESSING_TIME_"></span>What is the hardware certification submission processing time?

All hardware submissions to the dashboard will be processed within five business days or less, depending on whether the submission requires manual review. Manual review may be required if your submission's tests fail, if it does not have a valid filter applied, or due to internal business policy.

### <span id="Why_do_I_see_a_difference_in_download_signed_files_"></span><span id="why_do_i_see_a_difference_in_download_signed_files_"></span><span id="WHY_DO_I_SEE_A_DIFFERENCE_IN_DOWNLOAD_SIGNED_FILES_"></span>Why do I see a difference in download signed files?

In order to make Windows 10 more secure without affecting performance, all binaries are now receiving embedded signatures. This applies to all submissions for certification, not only Windows 10 submissions.

### <span id="How_to_get_a_single_cat_file_if_drivers_are_uniform_for_all_operating_systems"></span><span id="how_to_get_a_single_cat_file_if_drivers_are_uniform_for_all_operating_systems"></span><span id="HOW_TO_GET_A_SINGLE_CAT_FILE_IF_DRIVERS_ARE_UNIFORM_FOR_ALL_OPERATING_SYSTEMS"></span>How to get a single cat file if drivers are uniform for all operating systems

Make sure your final package has a single driver folder on the **Package** tab and the driver’s properties include all the operating systems you have tested. For more information, see [Walkthrough: How to get a driver signed by Microsoft for multiple versions of Windows](get-drivers-signed-by-microsoft-for-multiple-windows-versions.md).

### <span id="I_m_unable_to_add_new_marketing_names_to_the_approved_submission"></span><span id="i_m_unable_to_add_new_marketing_names_to_the_approved_submission"></span><span id="I_M_UNABLE_TO_ADD_NEW_MARKETING_NAMES_TO_THE_APPROVED_SUBMISSION"></span>I'm unable to add new marketing names to the approved submission

Check the announcement date that has been set. If the announcement date has passed, you won't be able to add a new name.

### How can I share a link to a Windows Certification Verification Report?
-   A sharable URL contains three identification numbers separated by slashes as shown below: `https://developer.microsoft.com/dashboard/hardware/driver/DownloadCertificationReport/SellerID/PrivateProductID/SubmissionID`

- The identification numbers used in the URL, and their locations are as follows:

| Component | Description |
| ---       | ---         |
|SellerID   | The identification number of your partner account. This can be found on the account management page, under **Account settings**. |
|PrivateProductID | The identification number generated with each product creation. Located on the driver details page for your product. See [Dashboard ID definitions](https://docs.microsoft.com/windows-hardware/drivers/dashboard/id-definitions) for more information. |
|SubmissionID | The idenfication number given to each submission and submission update. Located on the driver details page for your product. See [Dashboard ID definitions](https://docs.microsoft.com/windows-hardware/drivers/dashboard/id-definitions) for more information. |

- To create a sharable link, replace **SellerID**, **PrivateProductID**, and **SubmissionID** in the example URL above with the appropriate identification numbers.
- This URL allows the report to be accessed and downloaded without prior authorization or access to the Windows Hardware Dev Center Dashboard.   


## <span id="Troubleshooting_submission_upload_errors"></span><span id="troubleshooting_submission_upload_errors"></span><span id="TROUBLESHOOTING_SUBMISSION_UPLOAD_ERRORS"></span>Troubleshooting submission upload errors


### <span id="My_driver_signing_submission_fails_with_the_error__There_are_files_at_the_root_of_the_cabinet__or___No_.inf_files_found_in_driver_directory_directories__XYZ_"></span><span id="my_driver_signing_submission_fails_with_the_error__there_are_files_at_the_root_of_the_cabinet__or___no_.inf_files_found_in_driver_directory_directories__xyz_"></span><span id="MY_DRIVER_SIGNING_SUBMISSION_FAILS_WITH_THE_ERROR__THERE_ARE_FILES_AT_THE_ROOT_OF_THE_CABINET__OR___NO_.INF_FILES_FOUND_IN_DRIVER_DIRECTORY_DIRECTORIES__XYZ_"></span>My driver signing submission fails with the error “There are files at the root of the cabinet” or “\#No .inf files found in driver directory/directories: XYZ”

The failure is caused by an incorrect .cab file structure. The .cab structure was created with driver files in the root folder of the .cab file instead of having them in a subfolder. See [Attestation signing a kernel driver for public release](attestation-signing-a-kernel-driver-for-public-release.md) for instructions on how to create a proper .cab file for your driver signing submission.

### <span id="_It_looks_like_your_package_is_corrupt_or_missing_important_information._Ensure_you_are_using_the_latest_version_of_the_kit__regenerate_your_package__and_try_again._If_you_continue_to_experience_the_issue__contact_Support._"></span><span id="_it_looks_like_your_package_is_corrupt_or_missing_important_information._ensure_you_are_using_the_latest_version_of_the_kit__regenerate_your_package__and_try_again._if_you_continue_to_experience_the_issue__contact_support._"></span><span id="_IT_LOOKS_LIKE_YOUR_PACKAGE_IS_CORRUPT_OR_MISSING_IMPORTANT_INFORMATION._ENSURE_YOU_ARE_USING_THE_LATEST_VERSION_OF_THE_KIT__REGENERATE_YOUR_PACKAGE__AND_TRY_AGAIN._IF_YOU_CONTINUE_TO_EXPERIENCE_THE_ISSUE__CONTACT_SUPPORT._"></span>"It looks like your package is corrupt or missing important information. Ensure you are using the latest version of the kit, regenerate your package, and try again. If you continue to experience the issue, contact Support."

If you continue to experience issues with your package submission, contact Support in the dashboard header.

### <span id="File_is_using_Zip64_4gb_file_Size_"></span><span id="file_is_using_zip64_4gb_file_size_"></span><span id="FILE_IS_USING_ZIP64_4GB_FILE_SIZE_"></span>"File is using Zip64(4gb+file Size)"

This error is caused when the uploaded archive's filetype is .zip64 instead of .zip. This is caused by a large filesize. To fix this error, repackage the submission using the below steps.

1.  Rename the current .hckx/hlkx file to .zip.
2.  Extract to a folder.
3.  Open the folder.
4.  Select all items, then right-click and select **Send to Compressed zip folder**.
5.  Rename the new .zip folder as .hckx/.hlkx.
6.  Upload the new .hckx/.hlkx file.

### <span id="The_DUA_package_error_shows__Failed_to_open_package__with_the_error__Not_compatible_with_a_version__3.2.0.0__with_this_instance_package_manager_"></span><span id="the_dua_package_error_shows__failed_to_open_package__with_the_error__not_compatible_with_a_version__3.2.0.0__with_this_instance_package_manager_"></span><span id="THE_DUA_PACKAGE_ERROR_SHOWS__FAILED_TO_OPEN_PACKAGE__WITH_THE_ERROR__NOT_COMPATIBLE_WITH_A_VERSION__3.2.0.0__WITH_THIS_INSTANCE_PACKAGE_MANAGER_"></span>The DUA package error shows "Failed to open package" with the error “Not compatible with a version (3.2.0.0) with this instance package manager”

-   Use [HLK studio](https://msdn.microsoft.com/library/windows/hardware/dn939927) to open the downloaded DUA shell package and to create DUA submission.

 

 

