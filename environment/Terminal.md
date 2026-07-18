# Terminal

## Custom Prompt

- [Starship](https://starship.rs/)
  - Preset [Nerd Font Symbols Preset](https://starship.rs/presets/nerd-font.html)
  - [Nerd Font](https://www.nerdfonts.com/) used: Fira Code Nerd Font

- [zimfw](https://github.com/zsh-users/zimfw)
  - Installed via [SetupLinux.sh](SetupLinux.sh)

## Vim

- **Configuration:** [.vimrc](https://github.com/BradNut/dotfiles/blob/master/.vimrc)
- **Install:*** **Linux:** `sudo apt install vim`
* **OSX:** `brew install vim`

### Things to look into for Vim

- **Package Manager:** Consider using a plugin manager like [Vundle](https://github.com/VundleVim/Vundle.vim) or [vim-plug](https://github.com/junegunn/vim-plug).
- **Rainbow Parentheses:** [Rainbow Parentheses](https://github.com/frazrepo/vim-rainbow) can enhance readability.

## Zsh

_Currently using zsh_

- Install if not there
  - Linux/Ubuntu: `sudo apt install zsh`
  - macOS: `brew install zsh`

### Configuration

- **.zshrc**: [Link to .zshrc](https://github.com/BradNut/dotfiles/blob/master/.zshrc)
- **Oh My Zsh**: [Link to Oh My Zsh installation](https://ohmyzsh.sh)
  - Install: `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
- **.nvmrc**: [Link to .nvmrc](https://github.com/BradNut/dotfiles/blob/master/.nvmrc) - Node Version Manager config file

#### Oh My Zsh Plugins

- **Z**: [Link to Z plugin](https://github.com/agkozak/zsh-z)
  - Install: `git clone https://github.com/agkozak/zsh-z $ZSH_CUSTOM/plugins/zsh-z`
- **zsh-autosuggestions**: [Link to zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
  - Install: `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`
- **zsh-syntax-highlighting**: [Link to zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
  - Install: `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`


## SSH

### Enable

To enable SSH on your new machine, follow these steps:

1. Update the package list:
    ```sh
    $ sudo apt update
    ```

2. Install the `openssh-server` package:
    ```sh
    $ sudo apt install openssh-server
    ```

3. Verify that SSH is running:
    ```sh
    $ sudo systemctl status ssh
    ```

### Generating SSH Keys

To generate new SSH keys and add them to the SSH agent, follow these steps:

1. Generate a new SSH key pair (if you don't already have one):
    ```sh
    $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
    - This command will create a new RSA key with a 4096-bit length and associate it with your email.

2. Add the SSH key to the SSH agent:
    ```sh
    $ eval "$(ssh-agent -s)"
    $ ssh-add ~/.ssh/id_rsa
    ```

3. Copy the public key to your clipboard:
    ```sh
    $ cat ~/.ssh/id_rsa.pub
    ```

4. Add the public key to GitHub:
    - Go to your GitHub account settings.
    - Navigate to `SSH and GPG keys`.
    - Click on `New SSH key`.
    - Enter a title for the key (e.g., "Your Machine Name").
    - Paste the public key into the key field.
    - Click `Add SSH key`.
