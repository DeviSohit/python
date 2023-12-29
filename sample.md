# Heading 1
- Orange
- Apple
- Banana
* pine apple
* papaya

## Heading 2
1. First
2. Second

- [Devi github ](https://github.com/DeviSohit)
- ![Alt text](sg.jpg)
- ![Alt text](https://lh6.googleusercontent.com/OtH6zspEZfWi7binmpgNzBUjQ0axmErhB7o_9KCJHfv9TczOd0DaD1E-6QB772_Y-CE2R2rH-XNWZPeaxrz7ugY=w1280)

### Heading 3
To write a command: `sh helloworld.sh`

#### Heading 4

```yaml
- name: Install cart component
  hosts: cart
  become: yes
  tasks:
  - name: setup NPM source
    ansible.builtin.shell: "curl -sL https://rpm.nodesource.com/setup_lts.x | bash"

  - name: Install NodeJS
    ansible.builtin.yum:
      name: nodejs
      state: installed
```

##### Heading 5

###### Heading 6
