class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sentemails = set()
        for email in emails:
            local, domain= email.split("@")
            local = local.replace(".", "")
            plus = local.find("+")
            if plus != -1:    
                local = local[:plus]
            sentemails.add(local+"@"+domain)
        return len(sentemails)