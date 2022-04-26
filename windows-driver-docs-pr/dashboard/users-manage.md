---
title: Manage users
ms.topic: article
description: Manage users
ms.date: 04/20/2017
---


# Manage dashboard users

This article describes how you can use Partner Center User Management to manage your Hardware dashboard users.

The Partner Center uses Azure Active Directory for user management. For some actions, such as creating a new user or deleting a user, you'll need to use your developer portal Global Admin account credentials. The Global Admin account is the account that was used to register for the Hardware program. If your account was migrated from Sysdev, your Global Admin was notified via e-mail. If you've lost or are unsure of your Global Admin credentials, please contact support.  The developer portal Global Admin account credentials are not the same as the Azure AD Global Admin account credentials.


## Add existing users

To add existing users, you'll need to have the Manager role assigned to your Partner Center account.
As a user with the Manager role in Partner Center, you can add any user who is already associated with your Azure Active Directory tenant.

To add existing users:

1. Sign into [Partner Center Account settings](https://go.microsoft.com/fwlink/?linkid=833506) with an account that has the Manager role in Partner Center.

1. On the left menu, select **User management**.

1. Select **+ Add user**
   :::image type="content" source="images/managing-user-roles/user-management-add-user.png" alt-text="Screenshot that shows where to select '+ Add user' to add a user.":::

1. Search for and then select the users that you wish to add.

1. Select **Add Selected** at the top of the page.

## Create a new user

To create a new user, you'll need to sign in with your Global Admin account credentials.

To create a new user:

1. Sign into [Partner Center Account settings](https://go.microsoft.com/fwlink/?linkid=833506) as the Global Admin account.

1. On the left menu, select **User management**.

1. Select **+ Create new user**

1. Enter the details for your new user. You'll need their first and last names, as well as a custom user name that they'll use to login. You can also add them to any groups you’ve already created in your directory. Finally, you can grant them any roles they need for the Hardware Program.

   :::image type="content" source="images/managing-user-roles/user-management-roles.png" alt-text="Screenshot that shows the new user screen, and the details required for registering a new user.":::

1. Select **Save**. This will add the user to your account with the selected permission, and generate a one-time use password.

    >![!IMPORTANT]
    > Make sure you print or save this page for the new user. You will not be able to recover this password after > you leave this page.

## Invite users

To invite users, you'll need to sign in with your Global Admin account credentials.

To invite users:

1. Sign into [Partner Center Account settings](https://go.microsoft.com/fwlink/?linkid=833506) as the Global Admin account.

1. On the left menu, select **User management**.

1. Select **+Invite users**


## Change a user's role

For Hardware dashboard users, the following roles are available:

| Role                           | Description             |
|--------------------------------|--------------|
| Administrator     | Has complete control of your organization. Can manage roles in Dev Center and can complete any task.    |
| Upgrade Test Results Submitter | Can submit upgrade test results for your organization.    |
| Legal Agreement Signer         | Can renew and sign legal agreements on behalf of your organization.    |
| Report Reviewer                | Can access analytics about your drivers and systems. Able to see failure details and download cabs.   |
| Driver Submitter   | Can create new driver submissions, but can’t create shipping labels.   |
| Shipping Label Owner  | Can create and manage shipping labels, and can submit shipping labels including shipping labels with driver promotions (automatic installation) selected.   |
| System Submitter  | Can create new Systems Certifications and onboard new device definitions for the purposes of Upgrade Test result uploads. Can’t make changes to driver submissions or shipping labels.  |
| WCOS Image Signer | Sign WCOS system images.   |
| WCOS Retail Unlock | Generate retail unlock tokens for WCOS systems.    |
| Manager(Collaborate) | Can add users and make them a Manager for the Collaborate program.    |

To change a user's role, you'll need to have the Manager role assigned to your Partner Center account.

To change a user’s role:

1. Sign into [Partner Center Account settings](https://go.microsoft.com/fwlink/?linkid=833506) with an account that has the Manager role in Partner Center.

1. On the left menu, select **User management**.

1. In the search bar, type in the user you want to find.

   :::image type="content" source="images/managing-user-roles/user-management-search.png" alt-text="Screenshot that shows the search entry field for finding a user.":::

1. Select the name of the user.

1. In the user’s details, move through the page until you see **Roles applicable to developer programs**, and select the ones you want to assign to the user.

   :::image type="content" source="images/managing-user-roles/user-management-roles.png" alt-text="Screenshot that shows the various available for Hardware dashboard users.":::

1. Select **Update**.

## Delete users

To delete a user, you'll need to sign in with your Global Admin account credentials.

To delete users:

1. Sign into [Partner Center Account settings](https://go.microsoft.com/fwlink/?linkid=833506) as the Global Admin account.

1. On the left menu, select **User management**.

1. In the search bar, type in the user you want to find.

1. To the right of the name of the user, select **Delete**.

   :::image type="content" source="images/managing-user-roles/user-management-delete.png" alt-text="Screenshot that shows where to select 'Delete' to delete a user.":::
