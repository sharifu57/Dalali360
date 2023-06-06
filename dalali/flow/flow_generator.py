flow_lists = [
    {
        'name': 'Property',
        'code': 'WF1',
        'app': 'dalali',
        'model': 'Property',
        'main_object_app': 'dalali',
        'main_object_model': 'Property',
        'nodes': [
            {
                'name': 'start',
                'start': True,
                'end': False,
                'field_type': 'start',
                'view': ''
            },
            {
                'name': 'dalali',
                'start': False,
                'end': False,
                'field_type': 'node',
                'view': 'dalali.views.DalaliPropertyProcessing'
            }
        ]
    }
]