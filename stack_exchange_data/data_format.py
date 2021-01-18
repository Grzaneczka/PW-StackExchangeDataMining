""" Defines data format of the StackExchange data. """
from stack_exchange_data import converters

# Created based on:
# https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
STACK_EXCHANGE_DATA_FORMATS = {
    'badges': {
        'converters': {
            'Id': converters.to_numeric,
            'UserId': converters.to_numeric,
            'Class': converters.to_numeric,
            'TagBased': converters.string_to_bool,
        },
        'dtypes': {
            'Id': 'Int64',
            'UserId': 'Int64',
            'Name': 'string',
            'Date': 'datetime64',
            'Class': 'Int8',
            'TagBased': 'boolean',
        }
    },
    'comments': {
        'converters': {
            'Id': converters.to_numeric,
            'PostId': converters.to_numeric,
            'Score': converters.to_numeric,
            'UserId': converters.to_numeric
        },
        'dtypes': {
            'Id': 'Int64',
            'PostId': 'Int64',
            'Score': 'Int64',
            'Text': 'string',
            'CreationDate': 'datetime64',
            'UserDisplayName': 'string',
            'UserId': 'Int64',
            'ContentLicense': 'string'
        }
    },
    'posthistory': {
        'converters': {
            'Id': converters.to_numeric,
            'PostHistoryTypeId': converters.to_numeric,
            'PostId': converters.to_numeric,
            'UserId': converters.to_numeric,
        },
        'dtypes': {
            'Id': 'Int64',
            'PostHistoryTypeId': 'Int8',
            'PostId': 'Int64',
            'RevisionGUID': 'string',
            'CreationDate': 'datetime64',
            'UserId': 'Int64',
            'UserDisplayName': 'string',
            'Comment': 'string',
            'Text': 'string',
            'ContentLicense': 'string'
        }
    },
    'postlinks': {
        'converters': {
            'Id': converters.to_numeric,
            'PostId': converters.to_numeric,
            'RelatedPostId': converters.to_numeric,
            'LinkTypeId': converters.to_numeric,
        },
        'dtypes': {
            'Id': 'Int64',
            'CreationDate': 'datetime64',
            'PostId': 'Int64',
            'RelatedPostId': 'Int64',
            'LinkTypeId': 'Int8'
        }
    },
    'posts': {
        'converters': {
            'Id': converters.to_numeric,
            'PostTypeId': converters.to_numeric,
            'Score': converters.to_numeric,
            'AcceptedAnswerId': converters.to_numeric,
            'ParentId': converters.to_numeric,
            'ViewCount': converters.to_numeric,
            'OwnerUserId': converters.to_numeric,
            'LastEditorUserId': converters.to_numeric,
            'AnswerCount': converters.to_numeric,
            'CommentCount': converters.to_numeric,
            'FavoriteCount': converters.to_numeric,
        },
        'dtypes': {
            'Id': 'Int64',
            'PostTypeId': 'Int8',
            'AcceptedAnswerId': 'Int64',
            'ParentId': 'Int64',
            'CreationDate': 'datetime64',
            'Score': 'Int64',
            'ViewCount': 'Int64',
            'Body': 'string',
            'OwnerUserId': 'Int64',
            'OwnerDisplayName': 'string',
            'LastEditorUserId': 'Int64',
            'LastEditorDisplayName': 'string',
            'LastEditDate': 'datetime64',
            'LastActivityDate': 'datetime64',
            'Title': 'string',
            'Tags': 'string',
            'AnswerCount': 'Int64',
            'CommentCount': 'Int64',
            'FavoriteCount': 'Int64',
            'ClosedDate': 'datetime64',
            'CommunityOwnedDate': 'datetime64',
            'ContentLicense': 'string',
        }
    },
    'tags': {
        'converters': {
            'Id': converters.to_numeric,
            'Count': converters.to_numeric,
            'ExcerptPostId': converters.to_numeric,
            'WikiPostId': converters.to_numeric
        },
        'dtypes': {
            'Id': 'Int64',
            'TagName': 'string',
            'Count': 'Int64',
            'ExcerptPostId': 'Int64',
            'WikiPostId': 'Int64',
        }
    },
    'users': {
        'converters': {
            'Id': converters.to_numeric,
            'Reputation': converters.to_numeric,
            'Views': converters.to_numeric,
            'UpVotes': converters.to_numeric,
            'DownVotes': converters.to_numeric,
            'AccountId': converters.to_numeric
        },
        'dtypes': {
            'Id': 'Int64',
            'Reputation': 'Int64',
            'CreationDate': 'datetime64',
            'DisplayName': 'string',
            'LastAccessDate': 'datetime64',
            'WebsiteUrl': 'string',
            'Location': 'string',
            'AboutMe': 'string',
            'Views': 'Int64',
            'UpVotes': 'Int64',
            'DownVotes': 'Int64',
            'ProfileImageUrl': 'string',
            'AccountId': 'Int64'
        }
    },
    'votes': {
        'converters': {
            'Id': converters.to_numeric,
            'PostId': converters.to_numeric,
            'VoteTypeId': converters.to_numeric,
            'UserId': converters.to_numeric,
            'BountyAmount': converters.to_numeric
        },
        'dtypes': {
            'Id': 'Int64',
            'PostId': 'Int64',
            'VoteTypeId': 'Int8',
            'UserId': 'Int64',
            'CreationDate': 'datetime64',
            'BountyAmount': 'Int64'
        }
    },
}
