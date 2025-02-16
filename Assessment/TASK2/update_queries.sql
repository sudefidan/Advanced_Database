-- Update Address field

[
  {
        $set: {
            Address: {
                'Street': '$Street',
                'City': '$City',
                'Country': '$Country',
                'Zip Code': '$Zip Code'
            }
        }
    },
  {
    $unset: [
      'Street',
      'City',
      'Zip Code'
    ]
  }
]

-- Update favorite field
[
    {
        $set: {
            Favorite: {
                "Favorite Book": "$Favorite Book",
                "Favorite Drink": "$Favorite Drink",
                "Favorite Activity": "$Favorite Activity"
            }
        }
    },
    {
        $unset: [
            "Favorite Book",
            "Favorite Drink",
            "Favorite Activity"
        ]
    }
]


-- Update Neighbours field
[
    {
        $set: {
            Neighbours: [
                {
                    "Neighbour 1": "$Neighbour 1",
                    "Neighbour1Email": "$Neighbour1Email"
                },
                {
                    "Neighbour 2": "$Neighbour 2",
                    "Neighbour2Email": "$Neighbour2Email"
                }
            ]
        }
    },
    {
        $unset: [
            "Neighbour 1",
            "Neighbour1Email",
            "Neighbour 2",
            "Neighbour2Email"
        ]
    }
]