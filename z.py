class DemonstrationPermit:
    def __init__(self, permit_id, organizer, location, date, description):
        self.permit_id = permit_id
        self.organizer = organizer
        self.location = location
        self.date = date
        self.description = description

    def __str__(self):
        return f"Permit ID: {self.permit_id}, Organizer: {self.organizer}, Location: {self.location}, Date: {self.date}, Description: {self.description}"


class PermitManager:
    def __init__(self):
        self.permits = {}

    def add_permit(self, permit):
        self.permits[permit.permit_id] = permit

    def update_permit(self, permit_id, **kwargs):
        if permit_id in self.permits:
            for key, value in kwargs.items():
                setattr(self.permits[permit_id], key, value)
            return True
        else:
            return False

    def delete_permit(self, permit_id):
        if permit_id in self.permits:
            del self.permits[permit_id]
            return True
        else:
            return False

    def get_permit(self, permit_id):
        return self.permits.get(permit_id, None)


class ComplianceMonitor:
    def __init__(self):
        self.compliance_logs = {}

    def log_compliance(self, compliance_id, permit_id, is_compliant, details):
        self.compliance_logs[compliance_id] = {
            "permit_id": permit_id,
            "is_compliant": is_compliant,
            "details": details
        }

    def check_compliance(self, compliance_id):
        return self.compliance_logs.get(compliance_id, None)


import unittest

class TestPermitSystem(unittest.TestCase):
    def setUp(self):
        self.permit_manager = PermitManager()
        self.compliance_monitor = ComplianceMonitor()
        self.sample_permit = DemonstrationPermit(1, "ACME Corp", "Town Square", "2023-04-01", "Peaceful protest")

    def test_permit_crud_operations(self):
        self.permit_manager.add_permit(self.sample_permit)
        self.assertEqual(len(self.permit_manager.permits), 1)
        fetched_permit = self.permit_manager.get_permit(1)
        self.assertEqual(fetched_permit, self.sample_permit)
        self.assertTrue(self.permit_manager.update_permit(1, location="City Hall"))
        self.assertEqual(self.permit_manager.get_permit(1).location, "City Hall")
        self.assertTrue(self.permit_manager.delete_permit(1))
        self.assertIsNone(self.permit_manager.get_permit(1))

    def test_compliance_monitoring(self):
        self.compliance_monitor.log_compliance(101, 1, True, "All rules followed")
        self.assertTrue(self.compliance_monitor.check_compliance(101)['is_compliant'])

if __name__ == '__main__':
    unittest.main()
