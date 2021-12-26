class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
        return '[.]'.join(address.split('.'))
        return re.sub('\.', '[.]', address)
        return ''.join('[.]' if c == '.' else c for c in address)