class Connection:

    def __init__(self):
        self.xid=0

    def _start_transaction(self):
        print("Starting txn", self.xid)
        r = self.xid
        self.xid+=1
        return r

    def _commit_transaction(self, xid):
        print('committing txn', xid)

    def _rollback_transaction(self, xid):
        print('rollback txn', xid)
