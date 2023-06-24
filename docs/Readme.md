# Confluence APIs
---
## Users:
```python
def add_user(
    self,
    username: str,
    fullname: str,
    email: str,
    password: str = "Credential.NONE",
    notify_user: bool = False,
) -> requests.Response:
```
```python
def remove_user(self, username: str) -> requests.Response:
```
```python
def get_all_users(self, limit: int, start: int) -> dict:
```
## Groups:
```python
def add_group(self, group):
```
```python
def remove_group(self, group):
```
```python
def get_groups(self, **params) -> dict:
```
## Users & Groups:
```python
def add_user_to_group(self, username: str, group: str) -> requests.Response:
```
```python
def get_users_in_group(self, groupname: str, **params) -> dict:
```
```python
def remove_user_from_group(self, username: str, group: str) -> requests.Response:
```
