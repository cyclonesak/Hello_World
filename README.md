# Big Heading

This can be a general intro to the project.

## Smaller Heading

Talking about the first key point

###### Smallest heading

*Italics* v's **bold** v's plain old text

An example of a link: [Scott's Start Page](https://sak.free.nf/startpage/)

Text that is NOT a quote.

> Text that is.

Example of `code` insert ...

```
sudo apt update && sudo apt upgrade -y
```

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)

This info and more for formatting comes from [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

Or you can do it the easy way using [README.so](https://readme.so).

# Example of mermaid code

'''mermaid
erDiagram
    Parlor {
        ParlorID INT PK
        Name NVARCHAR(255) NOT NULL
        Location NVARCHAR(255) NOT NULL
    }

    Practitioner {
        PractitionerID INT PK
        Name NVARCHAR(255) NOT NULL
        Qualification NVARCHAR(255) NOT NULL
    }

    Therapy {
        TherapyID INT PK
        Name NVARCHAR(255) NOT NULL
        RequiredEquipment NVARCHAR(255) NOT NULL
    }

    Equipment {
        EquipmentID INT PK
        Name NVARCHAR(255) NOT NULL
    }

    Booking {
        BookingID INT PK
        StartDateTime DATETIME NOT NULL
        SessionLength INT NOT NULL
    }

    WorksAt {
        PractitionerID INT
        ParlorID INT
        PRIMARY KEY (PractitionerID, ParlorID)
    }

    Offers {
        TherapyID INT
        ParlorID INT
        PRIMARY KEY (TherapyID, ParlorID)
    }

    AvailableAt {
        EquipmentID INT
        ParlorID INT
        PRIMARY KEY (EquipmentID, ParlorID)
    }

    Parlor ||--o{ WorksAt
    Practitioner ||--o{ WorksAt
    Parlor ||--o{ Offers
    Therapy ||--o{ Offers
    Parlor ||--o{ AvailableAt
    Equipment ||--o{ AvailableAt
    Booking }|--o| Practitioner
    Booking }|--o| Therapy
    Booking }|--o| Parlor
'''
